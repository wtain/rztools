from io import StringIO
from typing import List

import requests
from requests.adapters import HTTPAdapter, Retry

from FindDuplicateFiles.FileEnumerator import FileEnumerator


# todo: rename to something like FileSystem or FSOperations
class RemoteFileEnumerator(FileEnumerator):

    def __init__(self, hostname: str, port: int, dir: str, timeout: int):
        self.hostname = hostname
        self.port = port
        self.dir = dir  # todo: move to get_files parameter
        self.timeout = timeout
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            method_whitelist=["HEAD", "GET", "OPTIONS"]
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.http = requests.Session()
        self.http.mount("https://", adapter)
        self.http.mount("http://", adapter)

    def get_files(self) -> List[str]:
        api_url = f"{self.hostname}:{self.port}/get_dir?path={self.dir}"
        return self.http.get(api_url, timeout=self.timeout).json()

    def open_binary(self, file_name: str):
        api_url = f"{self.hostname}:{self.port}/get_image?path={file_name}"
        stream = self.http.get(api_url, stream=True, timeout=self.timeout).raw
        return stream
        # data = requests.get(api_url)
        # file = StringIO(data)
        # return file

    def get_size(self, file_name: str) -> int:
        api_url = f"{self.hostname}:{self.port}/get_file_size?path={file_name}"
        # .content() - raw
        return int(self.http.get(api_url, timeout=self.timeout).json()["size"])
