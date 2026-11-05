from datetime import datetime


class Exam:
    test_id: int
    subject_id: int
    test_title: str
    test_date: datetime

    def __init__(self, test_id: int, subject_id: int, test_title: str, test_date: datetime):
        self.test_id = test_id
        self.subject_id = subject_id
        self.test_title = test_title
        self.test_date = test_date

    def get_subject_id(self):
        return self.subject_id

    def get_test_id(self):
        return self.test_id

    def get_test_title(self):
        return self.test_title

    def set_test_title(self, title: str):
        self.test_title = title