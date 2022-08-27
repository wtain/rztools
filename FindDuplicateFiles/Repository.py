import copy
import datetime
import uuid

from pymongo import MongoClient


class Repository:

    def __init__(self, mongoDbUrl: str, database_name: str, entity: str):
        self.client = MongoClient(mongoDbUrl)
        self.database = self.client[database_name]
        self.entity = self.database[entity]

    def create(self, object) -> uuid.UUID:
        id = uuid.uuid4()
        object_copy = copy.deepcopy(object)
        object_copy["id"] = str(id)
        object_copy["created_at"] = Repository.get_timestamp()
        self.entity.insert_one(object_copy)
        return id

    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().isoformat()

    def update(self, object):
        object["updated_at"] = Repository.get_timestamp()
        self.entity.find_one_and_update({"id": object["id"]},
                                       {"$set": object},
                                       upsert=True)

    @staticmethod
    def convert(object):
        return {
                 field: object[field] for field in object if field not in ["_id"]
               }

    def list(self):
        return self.output(self.entity.find())

    @staticmethod
    def output(iterator):
        return Repository.materialize(map(Repository.convert, iterator))

    @staticmethod
    def materialize(iterator):
        return list(iterator)
