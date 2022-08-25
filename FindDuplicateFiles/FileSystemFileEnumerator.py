import os
from typing import List

from FindDuplicateFiles.FileEnumerator import FileEnumerator


class FileSystemFileEnumerator(FileEnumerator):

    def __init__(self, directory: str):
        self.directory = directory

    def get_files(self) -> List[str]:
        result_files = []
        for root, dirs, files in os.walk(self.directory):
            fullFileNames = list(os.path.join(root, file) for file in files)
            result_files += fullFileNames
        return result_files

    def open_binary(self, file_name: str):
        return open(file_name, 'rb')

    def get_size(self, file_name: str) -> int:
        return os.path.getsize(file_name)
