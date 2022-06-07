import getopt
import sys


class RunSettings:
    def __init__(self):
        self.dir, self.blockSize = RunSettings.parseCommandLine()

    @staticmethod
    def parseCommandLine():
        argv = sys.argv[1:]

        root = '.'
        blockSize = None
        try:
            opts, args = getopt.getopt(argv, 'd:b:', ['dir', 'block_size'])
            opts = dict(opts)
            if opts.get('-d'):
                root = opts['-d']
            if opts.get('-b'):
                blockSize = int(opts['-b'])

        except getopt.GetoptError:
            sys.exit(2)
        return root, blockSize
