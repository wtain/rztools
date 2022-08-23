import json
from time import sleep

from flask import Flask, redirect, request
from flask_cors import CORS

from FindDuplicateFiles.file_repository import FileRepository
import threading
import atexit

import configparser


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


# config = configparser.RawConfigParser()
# config.read('app.properties')


# https://docs.python.org/2/library/configparser.html
# pool_time = int(config.get('Scheduler', 'scheduler.pool_time_seconds'))
# pool_time = 5


# variables that are accessible from anywhere
# commonDataStruct = {}
# lock to control access to variable
# dataLock = threading.Lock()
# thread handler
# yourThread = threading.Thread()


# def interrupt():
#     global yourThread
#     yourThread.cancel()
#
# # DOCS https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
#
# def doStuff():
#     # global commonDataStruct
#     # global yourThread
#     print("doStuff - before")
#     # with dataLock:
#     #     print("doStuff")
#         # Do your stuff with commonDataStruct Here
#
#     while True:
#         print("Working")
#         print(f"Sleeping {pool_time} seconds")
#         sleep(pool_time)
#
#     # Set the next thread to happen
#     # yourThread = threading.Timer(pool_time, doStuff, ())
#     # yourThread.start()
#
# def doStuffStart():
#     # Do initialisation stuff here
#     print("Starting")
#     # global yourThread
#     # Create your thread
#     # print("Creating")
#     # yourThread = threading.Timer(pool_time, doStuff, ())
#     # yourThread.start()
#     t = threading.Thread(target=doStuff, daemon=True)
#     t.start()

# print("Initializing")
# # Initiate
# doStuffStart()
# # When you kill Flask (SIGTERM), clear the trigger for the next thread
# atexit.register(interrupt)


if __name__ == "__main__":
    mongoUrl = f"mongodb://localhost:27017"
    print(f"Mongo DB endpoint: {mongoUrl}")
    print("Running")
    app.run(debug=True)
else:
    mongoUrl = f"mongodb://{mongo_host}:{port}"
    print(f"Mongo DB endpoint: {mongoUrl}")
    fileRepository = FileRepository(mongoUrl)
