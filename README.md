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
 cloud --domain public get test.csv
```


put: Uploads local file and returns a cloud url

get: Retrieves file and outputs to the console

append: (not yet implemented)

delete: (not yet implemented)