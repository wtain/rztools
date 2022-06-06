import getopt
import sys


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
