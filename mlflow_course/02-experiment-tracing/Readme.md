# MLFlow Server Setup with EC2, S3, and RDS

This project sets up an MLFlow server using Amazon EC2, S3, and RDS for artifact storage and metadata management.

## Description

This project provides a fully configured environment for running the MLFlow server on AWS, utilizing the following services:

* EC2: Hosts the MLFlow server, providing access to the web interface.
* S3: Used for storing artifacts such as models, data, and logs.
* RDS: A PostgreSQL database that stores MLFlow metadata, including experiment details, parameters, metrics, and more.
### Access the Server
The remote MLFlow server is accessible at:
http://ec2-13-60-23-89.eu-north-1.compute.amazonaws.com:8080

EC2 Setup for Running MLFlow Server
On the EC2 instance, the MLFlow server is started with the following command:

```bash
mlflow server -h 0.0.0.0 -p 8080 \
    --backend-store-uri postgresql:DB_USER:DB_PASSWORD@DB_ENDPOINT:5432/DB_NAME \
    --default-artifact-root s3://S3_BUCKET_NAME
```
* backend-store-uri: Specifies the PostgreSQL database on RDS where MLFlow metadata is stored.
* default-artifact-root: Specifies the S3 bucket used for storing artifacts.

## Summary

This project creates a fully functional infrastructure for managing machine learning experiments using MLFlow, providing a convenient environment for storing data, artifacts, and metadata, while also providing access to a web interface for monitoring and managing models.