class Subject:
    subject_id: int
    subject_name: str

    def __init__(self, subject_id: int, subject_name: str):
        self.subject_id = subject_id
        self.subject_name = subject_name

    def get_subject_id(self) -> int:
        return self.subject_id

    def get_subject_name(self):
        return self.subject_name

    def set_subject_name(self, subject_name: str):
        self.subject_name = subject_name