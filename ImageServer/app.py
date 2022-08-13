import argparse
import getopt
import json
import sys

from flask import Flask
from FindDuplicateFiles.file_repository import FileRepository

mongo_host = "duplicates_store"
# mongo_host = "localhost"
port = 27017

# argv = sys.argv[1:]

# try:
#     opts, args = getopt.getopt(argv, 'h:p:', ['host', 'port'])
#     opts = dict(opts)
#     if opts.get('-h'):
#         mongo_host = opts['-h']
#     if opts.get('-p'):
#         port = int(opts['-p'])
# except getopt.GetoptError as e:
#     print(f"Failed parsing command line: {e.msg}")

# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('--h', type=ascii,
#                     help='MongoDB host')
# parser.add_argument('--p', type=int,
#                     help='MongoDB port')
# args = parser.parse_args()
# mongo_host = args.host or mongo_host
# port = args.port or port

# def parse_commandline():
#     argv = sys.argv[1:]
#     values = {}
#     key = ""
#     for k in argv:
#         if k[0] == '-':
#             key = k[1:]
#         else:
#             values[key] = k
#     return values
#
#
# values = parse_commandline()
# mongo_host = values["m"] or mongo_host
# port = values["p"] or port
#



app = Flask(__name__)

@app.route('/view')
def view():
    fileRepository = FileRepository(mongoUrl)
    return json.dumps(fileRepository.list_files())

@app.route('/')
def hello_geek():
    return '<h1>Hello from Flask & Docker</h1>'


if __name__ == "__main__":
    mongoUrl = f"mongodb://localhost:27017"
    print(f"Mongo DB endpoint: {mongoUrl}")
    print("Running")
    app.run(debug=True)
else:
    mongoUrl = f"mongodb://{mongo_host}:{port}"
    print(f"Mongo DB endpoint: {mongoUrl}")
