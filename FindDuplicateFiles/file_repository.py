
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
                 "created": file['_id'].generation_time.strftime("%Y%m%d %H%M%S"),
                 "lastUpdated": file['lastUpdated'].strftime("%Y%m%d %H%M%S"),
                 "size": file['size'],
                 "tags": file['tags'],
               }

    def list_files(self):
        return self.output(self.files.find())

    def list_files_on_page(self, page_size: int, page_number: int):
        return self.output(self.apply_pagination(self.files.find(), page_number, page_size))

    @staticmethod
    def output(iterator):
        return list(map(FileRepository.convert_file_info, iterator))

    @staticmethod
    def apply_pagination(iterator, page_number: int, page_size: int):
        # if page_number == 1:
        #     return iterator.limit(page_size)
        nskip = (page_number - 1) * page_size
        print(f"Skipping {nskip}, page size = {page_size}")
        return iterator.skip(nskip).limit(page_size)

    def count_files(self):
        return self.files.count_documents({})

    def count_pages(self, page_size: int):
        return (self.count_files() - 1) // page_size + 1

