import hashlib


class FileRegistry:

    def __init__(self):
        self.registry = {}

    def visitFile(self, fullFileName: str):
        fileHash = self.calculateHash(fullFileName)
        fileList = self.registry.get(fileHash)
        if fileList:
            fileList.append(fullFileName)
        else:
            self.registry[fileHash] = [fullFileName]

    def calculateHash(self, file: str) -> str:
        BLOCK_SIZE = 65536

        file_hash = hashlib.sha256()
        with open(file, 'rb') as f:
            fb = f.read(BLOCK_SIZE)
            while len(fb) > 0:
                file_hash.update(fb)
                fb = f.read(BLOCK_SIZE)

        return file_hash.hexdigest()

    def printStatistics(self):
        duplicateClassesCount = 0
        etriesToRemoveCount = 0
        for fileHash, l in self.registry.items():
            count = len(l)
            if count > 1:
                duplicateClassesCount += 1
                etriesToRemoveCount += count - 1
                print('-------------------------------------------------')
                print(fileHash, ' ', count)
                for fileName in l:
                    print(fileName)
        print('Duplicate classes count ', duplicateClassesCount)
        print('Entries to remove count ', etriesToRemoveCount)
