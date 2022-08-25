import hashlib

from FindDuplicateFiles.FileEnumerator import FileEnumerator


class HashCalculator:

    def __init__(self, blockSize, file_enumerator: FileEnumerator):
        # todo: Change prints to Feedback interface usage
        print("Hash calculator block size: ", blockSize)
        self.blockSize = blockSize
        self.file_enumerator = file_enumerator

    def calculateHash(self, file: str) -> str:
        file_hash = hashlib.sha256()
        with self.file_enumerator.open_binary(file) as f:
            fb = f.read(self.blockSize)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(self.blockSize)

        return file_hash.hexdigest()
