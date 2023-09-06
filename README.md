[![CrowdStrike](/docs/asset/cs-logo.png)](https://www.crowdstrike.com)

[![CrowdStrike Subreddit](https://img.shields.io/badge/-r%2Fcrowdstrike-white?logo=reddit&labelColor=gray&link=https%3A%2F%2Freddit.com%2Fr%2Fcrowdstrike)](https://reddit.com/r/crowdstrike)


# AWS Lambda Function for Parquet to JSON Conversion and Falcon LogScale Integration

This AWS Lambda function is designed to be triggered by an S3 bucket event when a new **.parquet** file is created/uploaded. It converts the contents of the parquet file to json format and sends the data to Falcon LogScale repository using an ingest (authentication) token.

## Prerequisites

Before you can deploy and use this Lambda function, you'll need the following:

1. An AWS account and AWS Lambda access.

2. An S3 bucket where your .parquet files are stored, and to trigger the Lambda function when new files are uploaded.

3. The necessary AWS IAM roles and permissions to access S3 and Lambda.

4. A Falcon LogScale account with a repository and ingest token for authentication.


## Deployment

Follow these steps to deploy the Lambda function:

1. Clone this GitHub repository to your local environment.

2. Customize the Lambda function code to suit your specific requirements. Ensure that the code correctly reads .parquet files and sends data to Falcon LogScale using the token.

3. Package your Lambda function code and its dependencies into a ZIP file.

4. Create a new Lambda function in the AWS Lambda console.

5. Configure the trigger for the Lambda function to be the S3 bucket that notifies on new .parquet file uploads.

6. Ensure that the Lambda function has the necessary IAM permissions to access S3 and any other AWS services required.

7. Set environment variables for the Lambda function, including the Falcon LogScale ingest token and api endpoint.

8. Deploy the Lambda function by uploading the ZIP file.

#### Notes:
- Maximum zip size allowed by AWS Lambda funtion is 250mb.
- Please note this code uses fastparquet instead of pyarrow because of the size limit.

## Configuration

Configure the Lambda function using environment variables or configuration files as needed. Make sure to set the following variables:

- `baseUrl`: Falcon LogScale account url
- `logscaleToken`: Falcon LogScale API token for authentication.
-  other relevant configuration variables for your specific use case.

## Usage

Once the Lambda function is deployed and configured, it will automatically trigger whenever a new .parquet file is uploaded to the specified S3 bucket. The function will convert the file to JSON and send the data to Falcon LogScale.


**Useful Reference Links:**
  - [AWS Lambda Function Info](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

<p align="center"><img src="docs/asset/cs-logo-footer.png"><BR/><img width="150px" src="docs/asset/adversary-red-eyes.png"></P>
<h3><P align="center">WE STOP BREACHES</P></h3>
