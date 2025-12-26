import boto3
import csv
import io
from datetime import datetime
from collections import defaultdict

s3 = boto3.client('s3')

BUCKET = 'etl-project12'
INPUT_KEY = 'input/superstore.csv'
OUTPUT_KEY = 'output/top_10_profitable_products.csv'

def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

def parse_date(date_str):
    formats = (
        '%m/%d/%Y',
        '%d-%m-%Y',
        '%m-%d-%Y',
        '%Y-%m-%d'
    )
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None

def lambda_handler(event, context):

    response = s3.get_object(
        Bucket=BUCKET,
        Key=INPUT_KEY
    )

    content = response['Body'].read().decode('latin1')
    reader = csv.DictReader(io.StringIO(content))

    profit_by_product = defaultdict(float)

    for row in reader:
        sales = safe_float(row.get('Sales'))
        profit = safe_float(row.get('Profit'))
        product = row.get('Product Name')
        order_date = parse_date(row.get('Order Date'))

        if sales is None or profit is None or product is None or order_date is None:
            continue

        if sales > 0:
            profit_by_product[product] += profit

    # Sort and select top 10
    top_10 = sorted(
        profit_by_product.items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]

    output_buffer = io.StringIO()
    writer = csv.writer(output_buffer)
    writer.writerow(['product_name', 'total_profit'])

    for product, profit in top_10:
        writer.writerow([product, round(profit, 2)])

    s3.put_object(
        Bucket=BUCKET,
        Key=OUTPUT_KEY,
        Body=output_buffer.getvalue().encode('utf-8')
    )

    return {
        "statusCode": 200,
        "message": "Top 10 profitable products generated successfully"
    }
