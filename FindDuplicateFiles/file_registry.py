import os
import datetime
from typing import Dict

from FindDuplicateFiles.file_repository import FileRepository
from FindDuplicateFiles.image_tag_extractor import ImageTagExtractor


class FileRegistry:

    def __init__(self, hashCalculator, fileRepository: FileRepository, imageTagExtractor: ImageTagExtractor):
        self.registry = {}
        self.hashCalculator = hashCalculator
        self.fileRepository = fileRepository
        self.imageTagExtractor = imageTagExtractor

    def visitFile(self, fullFileName: str):
        fileHash = self.hashCalculator.calculateHash(fullFileName)
        fileList = self.registry.get(fileHash)
        if fileList:
            fileList.append(fullFileName)
        else:
            self.registry[fileHash] = [fullFileName]
        ts = datetime.datetime.utcnow()
        self.fileRepository.store_file(
            self.build_file_entry(fileHash, fullFileName,
                                  os.path.getsize(fullFileName),
                                  ts, self.imageTagExtractor.extractTags(fullFileName)))

    def printStatistics(self):
        duplicateClassesCount = 0
        entriesToRemoveCount = 0
        sizeToSaveTotal = 0
        fileSizesMismatches = 0
        for fileHash, fileNames in self.registry.items():
            count = len(fileNames)
            fileSizes = list(map(os.path.getsize, fileNames))
            sizeToSave = sum(fileSizes) - max(fileSizes)
            if max(fileSizes) != min(fileSizes):
                fileSizesMismatches += 1
            sizeToSaveTotal += sizeToSave
            if count > 1:
                duplicateClassesCount += 1
                entriesToRemoveCount += count - 1
                print('-------------------------------------------------')
                print(fileHash, ' ', count)
                for fileName in fileNames:
                    print(fileName)
        print('Duplicate classes count: ', duplicateClassesCount)
        print('Entries to remove count: ', entriesToRemoveCount)
        print('Total size to save: ', sizeToSaveTotal)
        print('File sizes mismatches (possible hash collisions): ', fileSizesMismatches)

    @staticmethod
    def build_file_entry(fileHash: str, fileName: str, fileSize: int, timestamp, tags: Dict[str, str]):
        return {
            "hash": fileHash,
            "size": fileSize,
            "path": fileName,
            "lastUpdated": timestamp,
            "tags": list(map(lambda it: {"name": it[0], "value": it[1]}, tags.items()))
        }
