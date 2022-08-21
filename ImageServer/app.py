import json

from flask import Flask, redirect, request
from flask_cors import CORS

from FindDuplicateFiles.file_repository import FileRepository

mongo_host = "duplicates_store"
port = 27017

# todo: Extract hardcode into properties
# todo: Keep application code in the volume so that container is not required to be rebuilt

app = Flask(__name__)
CORS(app)

@app.route('/view')
def view():
    return json.dumps(fileRepository.list_files())

@app.route('/byhash')
def list_by_hash():
    hash = request.args.get('hash', type=str)
    return json.dumps(fileRepository.list_files_by_hash(hash))

@app.route('/')
def default():
    return redirect("/view")

@app.route('/hashes')
def list_hashes():
    return json.dumps(fileRepository.list_hashes())

@app.route('/duplicates')
def list_duplicates():
    return json.dumps(fileRepository.list_duplicates())

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
