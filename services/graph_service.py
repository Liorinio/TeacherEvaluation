import pandas as pd
import plotly.express as px
import numpy as np
from database.data_access_layer.score_dal import ScoreDAL
from database.data_access_layer.student_dal import StudentDAL


def failed_vs_passed(name_of_test: str , db: ScoreDAL | None):
    if db is None:
        print("db doesn't exist")
        return

    list_of_grades = db.get_grades_by_test_name(name_of_test)
    passed = len([grade for grade in list_of_grades if grade.get_score() > 54])
    failed = len([grade for grade in list_of_grades if grade.get_score() < 55])

    fig = px.bar(
        x=["Passed", "Failed"],
        y=[passed, failed],
        color=["Passed", "Failed"],
        color_discrete_map={"Passed": "green", "Failed": "red"},
        title="Test Results")

    fig.show()


def student_grade_graph(student_id: int, db: ScoreDAL | None):
    if db is not None:
        grades = db.get_grade_by_student_id(student_id)
        if grades is None:
            return

        test_names = []
        scores = []
        for grade in grades:
            test_names.append(grade.get_test_name())
            scores.append(grade.get_score())

        points = np.array(scores)
        fig = px.line(x=test_names, y=points, markers=True, title='grades of a specific student', category_orders={'x': test_names})
        fig.update_traces(marker=dict(size=10, symbol="circle", color="blue"),)

        fig.show()

def grade_bar_plot(test_name: str, db: ScoreDAL | None):
    if db is not None:
        scores = db.get_grades_by_test_name(test_name)
        scores_array = np.array([score.get_score() for score in scores])

        bins = [-1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        labels = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"]

        binned_data = pd.cut(scores_array, bins=bins, labels=labels)
        counts_df = binned_data.value_counts().sort_index().reset_index()
        counts_df.columns = ['Score Range', 'Count']

        fig = px.bar(counts_df, x='Score Range', y='Count', title="Scores (Custom Bins)")

        fig.show()


def grade_bar_plot_by_class(test_name: str, grade_level: str, grades_db: ScoreDAL | None, students_db: StudentDAL | None):
    if grades_db is not None and students_db is not None:
        scores = grades_db.get_grades_by_test_name(test_name) # list of scores of students who took the exam
        students = students_db.get_students_by_class(grade_level) # list of students in the class
        students_id = [student.get_student_id() for student in students]

        scores = [score for score in scores if score.get_student_id() in students_id]

        scores_array = np.array([score.get_score() for score in scores])

        bins = [-1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        labels = ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"]

        binned_data = pd.cut(scores_array, bins=bins, labels=labels)
        counts_df = binned_data.value_counts().sort_index().reset_index()
        counts_df.columns = ['Score Range', 'Count']

        fig = px.bar(counts_df, x='Score Range', y='Count', title="Scores (Custom Bins)")

        fig.show()

def avg_of_a_test(test_name: str, db: ScoreDAL | None):
    if db is not None:
        scores = db.get_grades_by_test_name(test_name)
        mean = np.mean(np.array([score.get_score() for score in scores]))
        print(f"The average score on {test_name} is {mean}")
        return mean
    return None

def median_of_a_test(test_name: str, db: ScoreDAL | None):
    if db is not None:
        scores = db.get_grades_by_test_name(test_name)
        median = np.median(np.array([score.get_score() for score in scores]))
        print(f"The median score on {test_name} is {median}")
        return median
    return None

def percent_25th_of_a_test(test_name: str, db: ScoreDAL | None):
    if db is not None:
        scores = db.get_grades_by_test_name(test_name)
        percent_25th = np.percentile(np.array([score.get_score() for score in scores]), 25)
        print(f"The 75 percent on {test_name} is {percent_25th}")
        return percent_25th
    return None

def percent_75th_of_a_test(test_name: str, db: ScoreDAL | None):
    if db is not None:
        scores = db.get_grades_by_test_name(test_name)
        percent_25th = np.percentile(np.array([score.get_score() for score in scores]), 75)
        print(f"The 75 percent on {test_name} is {percent_25th}")
        return percent_25th
    return None