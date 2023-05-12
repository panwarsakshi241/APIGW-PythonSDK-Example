from utility import create_integration,create_method,create_method_response,create_resource
from Config import config
from Deployment import deployment
import os

def CreateProxy(ResourcePath):
    try:
        #1. createResource
        parentID= config.PARENTID
        try:
            for path in ResourcePath:
                resource = create_resource.CreateResource(config.RESTAPI, 
                                                        parentID, 
                                                        path
                                                        )
                parentID= resource
            print("Resource ID:",resource)
            try:
                #2. CreateMethod
                method = create_method.CreateMethod(config.RESTAPI, 
                                                    resource, 
                                                    config.METHOD, 
                                                    config.AUTHORIZATION
                                                    )
                print("Create Method Response:",method)
                try:
                    #3. CreateIntegration
                    integration=create_integration.createIntegration(config.RESTAPI, 
                                                                     resource, 
                                                                     config.URI, 
                                                                     config.CONNECTION_ID
                                                                     )
                    print("Create Integration Response: ",integration)

                    try:
                        #4 CreateResponse
                        methodResponse= create_method_response.MethodResponse(config.RESTAPI, 
                                                                              resource
                                                                              )
                        print("Method Response:",methodResponse)
                        return methodResponse
                        try:
                            #Create Deployment
                            deploy= deployment.CreateDeployment(config.RESTAPI,
                                                                 os.environ.get('STAGEENV')
                                                                 )
                            return deploy
                        except Exception as dpex:
                        	return f"Deployment Exception: {dpex}"
                    except Exception as mrex:
                        return f"Exception Occurred while creating Response: {mrex}"
                except Exception as inex:
                    return f"Exception Occurred while creating Integration: {inex}"
            except Exception as mex:
                return f"Exception Occurred while creating Method: {mex}"
        except Exception as rex:
            return f"Exception Occurred while creating Resource: {rex}"
    except Exception as ex:
        return f"Exception Occurred: {ex}"