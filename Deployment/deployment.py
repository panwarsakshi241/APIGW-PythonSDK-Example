from Connection import client


client = client.CreateClient()

def CreateDeployment(rest_api, stage_name):
    Deployment_response = client.create_deployment(
        restApiId=rest_api,
        stageName=stage_name,
        stageDescription='Stage for POC.',
        description='Creating and Deploying the Authenticator Rest API using Python SDK',
        cacheClusterEnabled=False,
        tracingEnabled= False
        )
    return Deployment_response
