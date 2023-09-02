import boto3
import io
import os
import pandas as pd
import json
import requests
import datetime
import urllib.parse
import fastparquet

def lambda_handler(event, context):
    """Sample pure Lambda function"""
    print("The Lambda Function is executing")
    try:
        logscale_token = os.environ.get('logscaleToken')
        baseUrl = os.environ.get('baseUrl')
        buffer = io.BytesIO()
        s3 = boto3.resource("s3")
        print(f"buffer is {buffer} and type is :",type(buffer))
        # extract the bucket & key
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        decodedKey = urllib.parse.unquote_plus(key)
        object = s3.Object(bucket,decodedKey)
        print(f"File name is : {decodedKey}")
        object.download_fileobj(buffer)
        print("after download")
        df = pd.read_parquet(buffer)
        print(f"DF is : {df}")
        eventpayloads = json.loads(df.to_json(orient="records"))
        print("after buffer")

        header = {'Authorization': f'Bearer {logscale_token}', 'Content-Type': 'application/json',
                  'Accept': 'application/json'}
        time = d = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
        events = list()

        for eventPayload in eventpayloads:
            events.append({"timestamp": time, "attributes": eventPayload})

        payload = [{"tags": {"host": "logscaleEvents"},
                    "events": events
                    }]
        print(f"after event:{payload}  ")
        response = requests.post(baseUrl, headers=header, data=json.dumps(payload))
        print(response.text)
    except Exception as err:
        print(f"Exception in lambda function execution is: {err}")
