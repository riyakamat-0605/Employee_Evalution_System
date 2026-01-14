from employee_evaluation import calculate_average, assign_rating

def test_outstanding():
    avg = calculate_average(95, 95, 95)
    assert assign_rating(avg) == "Outstanding"

def test_excellent():
    avg = calculate_average(85, 85, 85)
    assert assign_rating(avg) == "Excellent"

def test_very_good():
    avg = calculate_average(70, 70, 70)
    assert assign_rating(avg) == "Very Good"

def test_good():
    avg = calculate_average(55, 55, 55)
    assert assign_rating(avg) == "Good"

def test_needs_improvement():
    avg = calculate_average(45, 45, 45)
    assert assign_rating(avg) == "Needs Improvement"

def test_unsatisfactory():
    avg = calculate_average(30, 30, 30)
    assert assign_rating(avg) == "Unsatisfactory"
