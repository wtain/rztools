from FindDuplicateFiles.file_repository import FileRepository
from FindDuplicateFiles.file_system_scanner import FileSystemScanner
from FindDuplicateFiles.hash_calculator import HashCalculator
from FindDuplicateFiles.run_settings import RunSettings
from FindDuplicateFiles.file_registry import FileRegistry

BLOCK_SIZE = 65536

mongoUrl = "mongodb://localhost:27017"

settings = RunSettings()
hashCalculator = HashCalculator(settings.blockSize or BLOCK_SIZE)
fileRepository = FileRepository(mongoUrl)
fileRegistry = FileRegistry(hashCalculator, fileRepository)
fileSystemScanner = FileSystemScanner(settings.dir)

fileSystemScanner.scan(fileRegistry.visitFile)
fileRegistry.printStatistics()
