import json
def extract(jsondata):
    with open('./pricing/azure.json','r') as jsonread:
        filedata=json.load(jsonread)
        print(filedata)