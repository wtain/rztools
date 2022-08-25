import os
from typing import Callable

from Common.tracktime import TrackTime
from FindDuplicateFiles import Feedback
from FindDuplicateFiles.FileEnumerator import FileEnumerator


class FileSystemScanner:

    def __init__(self, feedback: Feedback, file_enumerator: FileEnumerator):
        self.feedback = feedback
        self.file_enumerator = file_enumerator;

    @TrackTime
    def scan(self, fileVisitor: Callable[[str], None]):
        count = 0
        divisor = 1000
        for fullFileName in self.file_enumerator.get_files():
            count += 1
            fileVisitor(fullFileName)
            if count % divisor == 0:
                self.feedback.print(count)

        self.feedback.print(f"Processed {count} files")
