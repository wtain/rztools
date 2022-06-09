from pymongo import MongoClient


class FileRepository:

    def __init__(self, mongoDbUrl):
        self.client = MongoClient(mongoDbUrl)
        self.duplicates_store = self.client.duplicates_store
        self.files = self.duplicates_store.files

    def store_file(self, file):
        self.files.find_one_and_update({"path": file["path"]},
                                       {"$set": file},
                                       upsert=True)
