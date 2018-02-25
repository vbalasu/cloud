import argparse

parser = argparse.ArgumentParser(description='Command line interface for handling CSV files in the cloud')
parser.add_argument('command', help='put | get')
parser.add_argument('filename', help='Eg. test.csv', type=argparse.FileType('r'))
parser.add_argument('domain', help='Eg. public')
args = parser.parse_args()
print(args.filename.read())