from Connection import client
import os

client = client.CreateClient()

def createIntegration(rest_api, resource_id, URI, Connection_id):
    integration_r = client.put_integration(
        restApiId=rest_api,
        resourceId= resource_id,
        httpMethod='POST',
        type='HTTP_PROXY',
        integrationHttpMethod='POST',
        uri= URI,
        connectionType='VPC_LINK',
        connectionId=Connection_id,
        timeoutInMillis=29000,
        tlsConfig={
            'insecureSkipVerification': True
            }
    )
    return integration_r