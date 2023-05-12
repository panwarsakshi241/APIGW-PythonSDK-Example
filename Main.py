import CreateApiProxy
from Config import config

def createAuthenticatorAPI():
    resourcePath= config.AUTH_RESOURCE_PATH 
    return CreateApiProxy.CreateProxy(resourcePath)


if __name__ == '__main__':
    print(createAuthenticatorAPI())
