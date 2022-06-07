import os
from typing import Callable

from Common.tracktime import TrackTime


class FileSystemScanner:

    def __init__(self, dir: str):
        self.dir = dir

    @TrackTime
    def scan(self, fileVisitor: Callable[[str], None]):
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                fullFileName = os.path.join(root, file)
                fileVisitor(fullFileName)
