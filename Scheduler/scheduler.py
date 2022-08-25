import configparser
import os
import sys
import threading
import traceback
from time import sleep

# https://stackoverflow.com/questions/61613656/python-import-from-parent-directory-for-dockerize-structure

sys.path.append(os.path.abspath('../'))

from FindDuplicateFiles.Feedback import Feedback
from FindDuplicateFiles.RemoteFileEnumerator import RemoteFileEnumerator
from FindDuplicateFiles.scan_fs_task import ScanFsTask
from Scheduler.task_repository import TaskRepository

config = configparser.RawConfigParser()
config.read('app.properties')

pool_time = int(config.get('Scheduler', 'scheduler.pool_time_seconds'))

mongo_host = config.get('MongoDB', 'mongo.host')
port = int(config.get('MongoDB', 'mongo.port'))

files_host = config.get('Files', 'files.host')
files_port = int(config.get('Files', 'files.port'))

if "mongo_host" in os.environ:
    mongo_host = os.environ["mongo_host"]

if "port" in os.environ:
    port = int(os.environ["port"])

if "files_host" in os.environ:
    files_host = os.environ["files_host"]

if "files_port" in os.environ:
    files_port = int(os.environ["files_port"])

mongoUrl = f"mongodb://{mongo_host}:{port}"

printLock = threading.Lock()

def print_threadsafe(message):
    with printLock:
        print(message)

class TaskFeedback(Feedback):

    def __init__(self, task_repository: TaskRepository, task):
        self.task_repository = task_repository
        self.task = task

    def print(self, message: str):
        print_threadsafe(message)

    def report_progress(self, value: int):
        self.print(f"Progress: {value}")
        self.task["progress"] = value
        self.task_repository.update_task(self.task)


def worker():
    print_threadsafe("Worker thread started")
    print_threadsafe(f"Mongo DB endpoint: {mongoUrl}")
    task_repository = TaskRepository(mongoUrl)
    print_threadsafe("Repository created")
    while True:
        print_threadsafe("Scheduler tick")
        task = task_repository.take_task()
        # todo: add thread pool
        # todo: update status via Feedback interface - pass it
        if task:
            print_threadsafe(f"Got task {task}")
            if task["task"] == "scan":
                task_name = task["task"]
                print_threadsafe(f"Got task {task_name}")
                try:
                    feedback = TaskFeedback(task_repository, task)
                    file_enumerator = RemoteFileEnumerator(files_host, files_port, "j:\\My Drive\\Pictures")
                    fs_task = ScanFsTask(feedback, file_enumerator)
                    # todo: pass parameters
                    # fs_task.run(task["dir"], task["block_size"], mongoUrl)
                    # todo: pass host imageProvider url
                    fs_task.run(131072, mongoUrl)
                except Exception as e:
                    trace = traceback.format_exc()
                    message = f"{str(e)}: {trace}"
                    print_threadsafe(f"Failed: {message}")
                    task["status"] = "failed"
                    task["message"] = message
                    task_repository.update_task(task)
                    continue
                print_threadsafe("Done")
                task["status"] = "done"
                task_repository.update_task(task)
            else:
                task["status"] = "failed"
                task["message"] = "Unsupported"
                task_repository.update_task(task)
                print_threadsafe("Unknown task")
        else:
            print_threadsafe("No new tasks")

        print_threadsafe(f"Sleeping {pool_time} seconds")
        sleep(pool_time)


# worker_thread = threading.Thread(target=worker, daemon=True)
# worker_thread.start()

worker()
