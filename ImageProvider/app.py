import json
import os
from configparser import ConfigParser
from functools import reduce

from flask import Flask, request, make_response
from flask_cors import CORS
from flask import stream_with_context, request

# config = ConfigParser.RawConfigParser()
# config.read('app.properties')
#
# storage_root = config.get('General', 'storage.root')
from FindDuplicateFiles.FileSystemFileEnumerator import FileSystemFileEnumerator

app = Flask(__name__)
CORS(app)

chunk_size = 10 * 1024  # 10Kb

@app.route('/get_image')
def get_image():
    path = request.args.get('path', type=str)
    #with open(path, "rb") as binary_file:
    # binary_file = open(path, "rb")

    @stream_with_context
    def generate():
        with open(path, "rb") as binary_file:
            for data in iter(lambda: binary_file.read(chunk_size), []):
                yield data
                if not len(data):
                    break
        # response = make_response(data)
        # response.headers.set('Content-Type', 'image/jpeg')
        # return response

    response = app.response_class(generate())
    response.headers.set('Content-Type', 'image/jpeg')  # todo: set proper content type
    return response

@app.route('/get_file_size')
def get_file_size():
    file_name = request.args.get('path', type=str)
    return json.dumps({
        "size": os.path.getsize(file_name)
    })

@app.route('/get_dir')
def get_dir():
    dir = request.args.get('path', type=str)
    file_enum = FileSystemFileEnumerator(dir)
    result_files = file_enum.get_files()
    # todo: pagination for the result
    return json.dumps(result_files)


if __name__ == "__main__":
    app.run(debug=True, port=8000, threaded=True, host="0.0.0.0")

