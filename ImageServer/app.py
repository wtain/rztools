import argparse
import getopt
import json
import sys

from flask import Flask, redirect, request
from flask_cors import CORS

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

# todo: Extract hardcode into properties
# todo: Keep application code in the volume so that container is not required to be rebuilt

app = Flask(__name__)
CORS(app)

@app.route('/view')
def view():
    return json.dumps(fileRepository.list_files())

@app.route('/')
def default():
    return redirect("/view")

@app.route('/page')
def get_page():
    page_num = request.args.get('num', type=int)
    page_size = request.args.get('size', type=int)
    return json.dumps(fileRepository.list_files_on_page(page_size, page_num))

@app.route('/page_count')
def get_page_count():
    page_size = request.args.get('size', type=int)
    return json.dumps(fileRepository.count_pages(page_size))


if __name__ == "__main__":
    mongoUrl = f"mongodb://localhost:27017"
    print(f"Mongo DB endpoint: {mongoUrl}")
    print("Running")
    app.run(debug=True)
else:
    mongoUrl = f"mongodb://{mongo_host}:{port}"
    print(f"Mongo DB endpoint: {mongoUrl}")
    fileRepository = FileRepository(mongoUrl)
