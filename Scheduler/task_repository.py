import datetime
import uuid

from pymongo import MongoClient


class TaskRepository:

    def __init__(self, mongoDbUrl):
        self.client = MongoClient(mongoDbUrl)
        self.duplicates_store = self.client.duplicates_store
        self.tasks = self.duplicates_store.tasks

    def store_task(self, task):
        self.tasks.insert_one({"taskid": uuid.uuid4()},
                                       {"$set": task})

    def update_task(self, task):
        self.tasks.find_one_and_update({"taskid": task["taskid"],
                                        "created_at": datetime.datetime.now().isoformat()},
                                       {"$set": task},
                                       upsert=True)

    @staticmethod
    def convert_task(task):
        return {
                 "taskid": task['taskid'],
                 "status": task['status'],
                 "task": task['task'],
                 "created_at": task['created_at'],
               }

    def list_tasks(self):
        return self.output(self.tasks.find())

    @staticmethod
    def output(iterator):
        return TaskRepository.materialize(map(TaskRepository.convert_task, iterator))

    @staticmethod
    def materialize(iterator):
        return list(iterator)

