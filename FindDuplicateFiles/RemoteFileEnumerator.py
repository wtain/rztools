from typing import List

import requests

from FindDuplicateFiles.FileEnumerator import FileEnumerator


class RemoteFileEnumerator(FileEnumerator):

    def __init__(self, hostname: str, port: int, dir: str):
        self.hostname = hostname
        self.port = port
        self.dir = dir

    def get_files(self) -> List[str]:
        api_url = f"{self.hostname}:{self.port}/get_dir?path={self.dir}"
        return requests.get(api_url).json()
