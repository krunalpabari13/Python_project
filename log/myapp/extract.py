import json
from django.http import JsonResponse
def extract(jsondata):
    azureans=azure(jsondata)
    print(azureans)
    ans={
        "azure":azureans
    }
    return JsonResponse(ans)

def azure(jsondata):
    with open('./pricing/azure.json','r') as jsonread:
        filedata=json.load(jsonread)
        ans=0;
        for input in jsondata:
            for data in filedata:
                for items in data[input['source']]:
                    if input['source']=='VirtualMachine' or input['source']=='AzureKubernetesService':
                        if input['cpu']==items['numberOfCPUs'] and input['ram']==items['ramSize']:
                            ans+=input['hours']*items['hourlyPrice'];
                            
                            break;
                    elif input['source']=='database':
                        if items['databaseEngine']==input['engine'] and items['region']=='East US':
                            ans+=input['hours']*items['hourlyPrice']
                            break;
                    elif input['source']=='LoadBalancer':
                        if items['region']=='East US':
                          ans+=input['hours']*items['hourlyPrice'];
                          break;
                    elif input['source']=='AzureBackup':
                        if items['backupType']==input['backupType'] and items['storageSize']==input['storageSize']:
                            ans+=input['hours']*items['hourlyPrice'];
                            break;
        return ans