from FindDuplicateFiles.file_system_scanner import FileSystemScanner
from FindDuplicateFiles.run_settings import RunSettings
from FindDuplicateFiles.file_registry import FileRegistry

settings = RunSettings()

fileRegistry = FileRegistry()
fileSystemScanner = FileSystemScanner(settings.dir)

fileSystemScanner.scan(lambda fileName: fileRegistry.visitFile(fileName))
fileRegistry.printStatistics()
