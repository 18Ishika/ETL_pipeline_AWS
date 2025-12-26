# ETL_pipeline_AWS

# Athena ETL Project

This project demonstrates an ETL workflow using **AWS Athena**, **S3**, and **Lambda** to process and analyze data. The workflow extracts data from S3, transforms it using SQL and Lambda scripts, and stores the processed results back in S3 for querying via Athena.

---

## Project Overview

The goal of this project is to demonstrate an end-to-end ETL pipeline using AWS services. The pipeline processes raw data, performs transformations, and makes it queryable in Athena. This project is fully serverless and suitable for analysis of datasets stored in S3.

---

## Architecture

1. **Source Data**: Raw CSV files stored in S3.  
2. **ETL Process**: AWS Lambda (or SQL scripts) transform the data.  
3. **Querying**: AWS Athena reads processed data from S3.  
4. **Results**: Output CSVs stored back in S3.  


```

S3 Raw Data --> Lambda/SQL ETL --> S3 Processed Data --> Athena Query

````

---

## Technologies Used

- **AWS Athena** – Querying and analyzing structured data in S3  
- **AWS S3** – Storage for raw and processed datasets  
- **AWS Lambda** – Transforming data (ETL)  
- **SQL** – For data transformations and queries  

---


## Sample Output


<img width="983" height="562" alt="Screenshot 2025-12-26 132602" src="https://github.com/user-attachments/assets/f116e19f-7e96-4820-a16c-ed7ced9fc807" />


<img width="1258" height="480" alt="Screenshot 2025-12-26 130619" src="https://github.com/user-attachments/assets/06c2a93a-27c0-4858-aa19-0a00e1307d13" />

<img width="1349" height="486" alt="Screenshot 2025-12-26 130047" src="https://github.com/user-attachments/assets/6f1ca0da-1afb-43eb-9581-160c0f2da093" />



