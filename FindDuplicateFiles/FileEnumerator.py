from typing import List


class FileEnumerator:

    def get_files(self) -> List[str]:
        pass

    def open_binary(self, file_name: str):
        pass

    def get_size(self, file_name: str) -> int:
        pass
