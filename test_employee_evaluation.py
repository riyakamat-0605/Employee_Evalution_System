from employee_evaluation import calculate_rating


def test_outstanding():
    assert calculate_rating([95, 92, 94]) == "Outstanding"


def test_excellent():
    assert calculate_rating([85, 88, 82]) == "Excellent"


def test_very_good():
    assert calculate_rating([70, 75, 78]) == "Very Good"


def test_good():
    assert calculate_rating([55, 60, 58]) == "Good"


def test_needs_improvement():
    assert calculate_rating([45, 42, 48]) == "Needs Improvement"


def test_unsatisfactory():
    assert calculate_rating([30, 35, 38]) == "Unsatisfactory"
