import getopt
import sys
import hashlib
import os
from typing import List, Dict


class RunSettings:
    def __init__(self):
        self.dir = RunSettings.parseCommandLine()

    @staticmethod
    def parseCommandLine() -> str:
        argv = sys.argv[1:]

        root = '.'
        try:
            opts, args = getopt.getopt(argv, 'd:', ['dir'])
            opts = dict(opts)
            if opts.get('-d'):
                root = opts['-d']

        except getopt.GetoptError:
            sys.exit(2)
        return root


def calculateHash(file: str) -> str:
    BLOCK_SIZE = 65536

    file_hash = hashlib.sha256()
    with open(file, 'rb') as f:
        fb = f.read(BLOCK_SIZE)
        while len(fb) > 0:
            file_hash.update(fb)
            fb = f.read(BLOCK_SIZE)

    return file_hash.hexdigest()


settings: RunSettings = RunSettings()

registry: Dict[str, List[str]] = {}

for root, dirs, files in os.walk(settings.dir):
    path = root.split(os.sep)
    # print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        fullFileName = root + os.sep + file
        fileHash = calculateHash(fullFileName)
        fileList = registry.get(fileHash)
        if fileList:
            fileList.append(fullFileName)
        else:
            registry[fileHash] = [fullFileName]
        # print(len(path) * '---', file, ' ', calculateHash(root + os.sep + file))

for fileHash, l in registry.items():
    count = len(l)
    if count > 1:
        print('-------------------------------------------------')
        print(fileHash, ' ', count)
        for fileName in l:
            print(fileName)