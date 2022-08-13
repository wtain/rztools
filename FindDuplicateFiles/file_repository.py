
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

    @staticmethod
    def convert_file_info(file):
        return {
                 "path": file['path'],
                 "hash": file['hash'],
                 "lastUpdated": file['lastUpdated'].strftime("%Y%m%d %H%M%S"),
                 "size": file['size'],
                 "tags": file['tags'],
               }

    def list_files(self):
        return list(map(FileRepository.convert_file_info,
                        self.files.find()))
