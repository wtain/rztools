
from FileRegistry import FileRegistry
from FileSystemScanner import FileSystemScanner
from RunSettings import RunSettings

settings = RunSettings()

fileRegistry = FileRegistry()
fileSystemScanner = FileSystemScanner(settings.dir)

fileSystemScanner.scan(lambda fileName: fileRegistry.visitFile(fileName))
fileRegistry.printStatistics()
