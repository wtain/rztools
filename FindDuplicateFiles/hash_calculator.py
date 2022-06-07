import hashlib


class HashCalculator:

    def __init__(self, blockSize):
        print("Hash calculator block size: ", blockSize)
        self.blockSize = blockSize

    def calculateHash(self, file: str) -> str:
        file_hash = hashlib.sha256()
        with open(file, 'rb') as f:
            fb = f.read(self.blockSize)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(self.blockSize)

        return file_hash.hexdigest()
