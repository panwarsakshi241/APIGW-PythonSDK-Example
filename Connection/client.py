import boto3

def CreateClient():
    client = boto3.client('apigateway',region_name='us-west-2')
    return client

