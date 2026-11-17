import numpy as np
from src.database.data_access_layer.score_dal import ScoreDAL


def avg_of_a_test(test_name: str, db: ScoreDAL | None):
    if db is None:
        return None
    scores = db.get_grades_by_test_name(test_name)
    mean = np.mean(np.array([score.get_score() for score in scores]))
    print(f"The average score on {test_name} is {mean}")
    return mean


def median_of_a_test(test_name: str, db: ScoreDAL | None):
    if db is None:
        return None
    scores = db.get_grades_by_test_name(test_name)
    median = np.median(np.array([score.get_score() for score in scores]))
    print(f"The median score on {test_name} is {median}")
    return median


def percent_25th_of_a_test(test_name: str, db: ScoreDAL | None):
    if db is None:
        return None
    scores = db.get_grades_by_test_name(test_name)
    percent_25th = np.percentile(np.array([score.get_score() for score in scores]), 25)
    print(f"The 75 percent on {test_name} is {percent_25th}")
    return percent_25th


def percent_75th_of_a_test(test_name: str, db: ScoreDAL | None):
    if db is None:
        return None
    scores = db.get_grades_by_test_name(test_name)
    percent_25th = np.percentile(np.array([score.get_score() for score in scores]), 75)
    print(f"The 75 percent on {test_name} is {percent_25th}")
    return percent_25th