from Connection import client
import os

client = client.CreateClient()

def MethodResponse(rest_api,resource_id):
    response = client.put_method_response(
        restApiId=rest_api,
        resourceId=resource_id,
        httpMethod='POST',
        statusCode='200',
        responseModels={
            'application/json': 'Empty'
            }
        )
    return response