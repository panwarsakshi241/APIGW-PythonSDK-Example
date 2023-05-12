from Connection import client
import os

client = client.CreateClient() 

def CreateResource(restApi,parentId,path): 
    cr_response=client.create_resource(
        restApiId=restApi,
        parentId=parentId,
        pathPart=path
    )
    resource_id= cr_response['id']
    return resource_id