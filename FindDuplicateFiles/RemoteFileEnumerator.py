from io import StringIO
from typing import List

import requests

from FindDuplicateFiles.FileEnumerator import FileEnumerator


# todo: rename to something like FileSystem or FSOperations
class RemoteFileEnumerator(FileEnumerator):

    def __init__(self, hostname: str, port: int, dir: str, timeout: int):
        self.hostname = hostname
        self.port = port
        self.dir = dir # todo: move to get_files parameter
        self.timeout = timeout

    def get_files(self) -> List[str]:
        api_url = f"{self.hostname}:{self.port}/get_dir?path={self.dir}"
        return requests.get(api_url, timeout=self.timeout).json()

    def open_binary(self, file_name: str):
        api_url = f"{self.hostname}:{self.port}/get_image?path={file_name}"
        stream = requests.get(api_url, stream=True, timeout=self.timeout).raw
        return stream
        # data = requests.get(api_url)
        # file = StringIO(data)
        # return file

    def get_size(self, file_name: str) -> int:
        api_url = f"{self.hostname}:{self.port}/get_file_size?path={file_name}"
        # .content() - raw
        return int(requests.get(api_url, timeout=self.timeout).json()["size"])
