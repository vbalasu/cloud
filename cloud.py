import argparse
import json

def cloudGet(filename, domain):
    #https://cloudmaticafunctions.azurewebsites.net/api/cloudGet?code=m8Qpr9D0D/FyOatpL9jnCL34ZBtMBz1U04kp4n4dia9kAfhFjNWgVQ==
    import requests
    url = "https://cloudmaticafunctions.azurewebsites.net/api/cloudGet"
    querystring = {"code":"m8Qpr9D0D/FyOatpL9jnCL34ZBtMBz1U04kp4n4dia9kAfhFjNWgVQ==","filename":filename,"domain":domain}
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)

def cloudPut(filename, domain, contents):
    #https://cloudmaticafunctions.azurewebsites.net/api/cloudPut?code=SDSGxtRh2S5RrSW/aNiFfgTE1bJhMqof3aiFdp8p7iYMjns/mFes0A==
    import requests
    url = "https://cloudmaticafunctions.azurewebsites.net/api/cloudPut"
    querystring = {"code":"SDSGxtRh2S5RrSW/aNiFfgTE1bJhMqof3aiFdp8p7iYMjns/mFes0A=="}
    data = {"filename": filename, "domain": domain, "contents": contents}
    print(data)
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", url, headers=headers, params=querystring, json=data)
    print(response.text)

parser = argparse.ArgumentParser(description='Command line interface for handling CSV files in the cloud')
parser.add_argument('command', help='put | get')
parser.add_argument('filename', help='Eg. test.csv')
parser.add_argument('domain', help='Eg. public')
parser.add_argument('contents', help='Eg. test.csv', type=argparse.FileType('r'))
args = parser.parse_args()
print(args)

if args.command == 'put':
    cloudPut(args.filename, args.domain, args.contents.read())
else:
    cloudGet(args.filename, args.domain)
