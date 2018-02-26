# cloud

usage: cloud.py [-h] command filename domain [contents]

Command line interface for handling CSV files in the cloud

positional arguments:
  command     put | get
  filename    Eg. test.csv
  domain      Eg. public
  contents    Eg. test.csv  (Required if command is put)

optional arguments:
  -h, --help  show this help message and exit

USAGE EXAMPLES 
 python cloud.py put test.csv public test.csv 
 python cloud.py get test.csv 





put: Uploads local file and returns a cloud url
get: Retrieves file and outputs to the console