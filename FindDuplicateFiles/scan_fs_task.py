from FindDuplicateFiles.Feedback import Feedback
from FindDuplicateFiles.FileEnumerator import FileEnumerator
from FindDuplicateFiles.file_repository import FileRepository
from FindDuplicateFiles.file_system_scanner import FileSystemScanner
from FindDuplicateFiles.hash_calculator import HashCalculator
from FindDuplicateFiles.image_tag_extractor import ImageTagExtractor
from FindDuplicateFiles.file_registry import FileRegistry

class ScanFsTask:

    def __init__(self, feedback: Feedback, file_enumerator: FileEnumerator):
        self.feedback = feedback
        self.file_enumerator = file_enumerator

    def run(self, block_size: int, mongoUrl: str):
        hashCalculator = HashCalculator(block_size, self.file_enumerator)
        fileRepository = FileRepository(mongoUrl)
        imageTagExtractor = ImageTagExtractor(self.file_enumerator)
        fileRegistry = FileRegistry(hashCalculator, fileRepository, imageTagExtractor, self.file_enumerator)
        fileSystemScanner = FileSystemScanner(self.feedback, self.file_enumerator)

        fileSystemScanner.scan(fileRegistry.visitFile)
        fileRegistry.printStatistics()
