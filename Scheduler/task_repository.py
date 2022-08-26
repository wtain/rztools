import copy
import datetime
import uuid

from pymongo import MongoClient


class TaskRepository:

    def __init__(self, mongoDbUrl):
        self.client = MongoClient(mongoDbUrl)
        self.duplicates_store = self.client.duplicates_store
        # todo: move to self.client.tasks? - separate database
        self.tasks = self.duplicates_store.tasks

    def store_task(self, task) -> uuid.UUID:
        id = uuid.uuid4()
        task_copy = copy.deepcopy(task)
        task_copy["taskid"] = str(id)
        task_copy["created_at"] = TaskRepository.get_timestamp()
        self.tasks.insert_one(task_copy)
        # todo: updated_at, heart-beat
        return id

    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().isoformat()

    def update_task(self, task):
        task["updated_at"] = TaskRepository.get_timestamp()
        self.tasks.find_one_and_update({"taskid": task["taskid"]},
                                       {"$set": task},
                                       upsert=True)

    def create_task(self, task: str, parameters) -> uuid.UUID:
        return self.store_task({"task": task, "status": "created", "parameters": parameters})

    def take_task(self):
        task = self.tasks.find_one({"status": "created"})
        if not task:
            return None
        task["status"] = "running"
        self.update_task(task)
        return task

    @staticmethod
    def convert_task(task):
        fields = ["taskid", "status", "task", "created_at", "parameters", "message", "progress", "updated_at"]
        return {
                 field: task[field] for field in fields if field in task
               }

    def list_tasks(self):
        return self.output(self.tasks.find())

    @staticmethod
    def output(iterator):
        return TaskRepository.materialize(map(TaskRepository.convert_task, iterator))

    @staticmethod
    def materialize(iterator):
        return list(iterator)

