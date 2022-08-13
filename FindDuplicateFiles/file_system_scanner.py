import os
from typing import Callable

from Common.tracktime import TrackTime


class FileSystemScanner:

    def __init__(self, dir: str):
        self.dir = dir

    @TrackTime
    def scan(self, fileVisitor: Callable[[str], None]):
        count = 0
        divisor = 1000
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                count += 1
                fullFileName = os.path.join(root, file)
                fileVisitor(fullFileName)
                if count % divisor == 0:
                    print(F"*** {count} files processed so far...")

        print(f"Processed {count} files")
