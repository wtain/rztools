from FindDuplicateFiles.Feedback import Feedback


class ConsoleFeedback(Feedback):

    def print(self, message: str):
        print(message)

    def report_progress(self, value: int):
        self.print(f"Progress: {value}")
