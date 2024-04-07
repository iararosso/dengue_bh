import json
import boto3
import logging
import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def lambda_handler(event, context):
    try:
        if 'data' in event:
            data = json.loads(event['data'])  # Acessa os dados usando json.loads
            s3 = boto3.client('s3')
            bucket_name = "projeto-dengue-bh-raw"
            today_date = datetime.datetime.now().date()
            destination_directory = f'dados-semanais/extracted_at={today_date}/dados.csv'
            s3.put_object(Bucket=bucket_name, Key=destination_directory, Body=json.dumps(data))
            logging.info(f'Data for {today_date} was successfully sent and saved to {destination_directory}.')
            return {
                'statusCode': 200,
                'body': json.dumps('Data successfully sent to S3')
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Data key not found in the event')
            }
    except Exception as e:
        logging.error(f"Error sending data to S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {e}')
        }
