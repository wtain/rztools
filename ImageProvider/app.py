import json
import os
from configparser import ConfigParser
from functools import reduce

from flask import Flask, request, make_response
from flask_cors import CORS

# config = ConfigParser.RawConfigParser()
# config.read('app.properties')
#
# storage_root = config.get('General', 'storage.root')
from FindDuplicateFiles.FileSystemFileEnumerator import FileSystemFileEnumerator

app = Flask(__name__)
CORS(app)

@app.route('/get_image')
def get_image():
    path = request.args.get('path', type=str)
    with open(path, "rb") as binary_file:
        data = binary_file.read()
        response = make_response(data)
        response.headers.set('Content-Type', 'image/jpeg')
        return response

@app.route('/get_dir')
def get_dir():
    dir = request.args.get('path', type=str)
    file_enum = FileSystemFileEnumerator(dir)
    result_files = file_enum.get_files()
    # todo: pagination for the result
    return json.dumps(result_files)


if __name__ == "__main__":
    app.run(debug=True, port=8000)

