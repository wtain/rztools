from FindDuplicateFiles.ConsoleFeedback import ConsoleFeedback
from FindDuplicateFiles.FileSystemFileEnumerator import FileSystemFileEnumerator
from FindDuplicateFiles.run_settings import RunSettings
from FindDuplicateFiles.scan_fs_task import ScanFsTask

BLOCK_SIZE = 131072

mongoUrl = "mongodb://localhost:27017"

settings = RunSettings()


if __name__ == "__main__":
    feedback = ConsoleFeedback()
    file_enumerator = FileSystemFileEnumerator(settings.dir)
    task = ScanFsTask(feedback, file_enumerator)
    task.run(settings.blockSize or BLOCK_SIZE, mongoUrl)
