# cloud

```
usage: cloud [-h] [--domain DOMAIN] command filename

Command line interface for handling CSV files in the cloud

positional arguments:
  command          put | get
  filename         Eg. test.csv

optional arguments:
  -h, --help       show this help message and exit
  --domain DOMAIN  Eg. public

USAGE EXAMPLES 
 cloud put test.csv 
 cloud get test.csv
 cloud append test.csv
 cloud delete test.csv 
 cloud --domain public get test.csv
```


put: Uploads a local file and returns a cloud url

get: Retrieves a remote file and outputs to the console

append: Appends the contents of a local file to a remote file. This assumes that the remote file already exists

delete: Deletes a remote file

In addition to the command line interface, there are Javascript clients
 NodeJS: cloudClient.js
 Browser: cloudClientBrowser.js 