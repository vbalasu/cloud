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
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", url, headers=headers, params=querystring, json=data)
    print(response.text)

def cloudAppend(filename, domain, contents):
    #https://cloudmaticafunctions.azurewebsites.net/api/cloudAppend?code=WoQI74R74MsaMzqo3cxEV3AbU6IjzxyCdWMA/3VCBp8Iy9C14JUiHw==
    import requests
    url = "https://cloudmaticafunctions.azurewebsites.net/api/cloudAppend"
    querystring = {"code":"WoQI74R74MsaMzqo3cxEV3AbU6IjzxyCdWMA/3VCBp8Iy9C14JUiHw=="}
    data = {"filename": filename, "domain": domain, "contents": contents}
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", url, headers=headers, params=querystring, json=data)
    print(response.text)

def cloudDelete(filename, domain):
    #https://cloudmaticafunctions.azurewebsites.net/api/cloudDelete?code=0iDGJqrFf3zzCFkSRtkogamQUR848INQviaa/sNGKlLSSR9uics2CA==
    import requests
    url = "https://cloudmaticafunctions.azurewebsites.net/api/cloudDelete"
    querystring = {"code":"0iDGJqrFf3zzCFkSRtkogamQUR848INQviaa/sNGKlLSSR9uics2CA=="}
    data = {"filename": filename, "domain": domain}
    headers = {'cache-control': "no-cache"}
    response = requests.request("GET", url, headers=headers, params=querystring, json=data)
    print(response.text)

from argparse import RawTextHelpFormatter
epilog = 'USAGE EXAMPLES \n cloud put test.csv \n cloud get test.csv \n cloud --domain public get test.csv \n cloud append test.csv \n cloud delete test.csv'
parser = argparse.ArgumentParser(description='Command line interface for handling CSV files in the cloud', epilog=epilog, formatter_class=RawTextHelpFormatter)
parser.add_argument('command', help='put | get | append | delete')
parser.add_argument('filename', help='Eg. test.csv')
parser.add_argument('--domain', help='Eg. public', default='public')
args = parser.parse_args()
with open(args.filename) as f:
    contents = f.read()

if args.command == 'put':
    cloudPut(args.filename, args.domain, contents)
elif args.command == 'append':
    cloudAppend(args.filename, args.domain, contents)
elif args.command == 'delete':
    cloudDelete(args.filename, args.domain)
else:
    cloudGet(args.filename, args.domain)
