from pprint import pprint

from pymongo import MongoClient


class FileRepository:

    def __init__(self, mongoDbUrl):
        self.client = MongoClient(mongoDbUrl)
        self.duplicates_store = self.client.duplicates_store
        serverStatusResult = self.duplicates_store.command("serverStatus")
        pprint(serverStatusResult)
        self.files = self.duplicates_store.files

    def store_file(self, file):
        self.files.insert_one(file)
