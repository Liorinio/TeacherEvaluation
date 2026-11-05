from datetime import datetime


class TestGrade:
    student_id: int
    test_name: str
    score: int
    comments: str
    test_date: datetime

    def __init__(self, student_id: int, test_name: str, score: int, comments: str, test_date: datetime):
        self.student_id = student_id
        self.test_name = test_name
        self.update_evaluation(score, comments)
        self.test_date = test_date

    def get_test_name(self) -> str:
        return self.test_name

    def get_student_id(self) -> int:
        return self.student_id

    def __set_score__(self, score: int):
        self.score = max(0, min(score, 100))

    def __set_comments__(self, comments: str):
        self.comments = comments

    def update_evaluation(self, score: int, comments: str):
       self.__set_score__(score)
       if score > 100:
           self.__set_comments__(f"{score - 100} points bonus\n" + comments)
       else:
           self.__set_comments__(comments)

    def get_score(self):
        return self.score



