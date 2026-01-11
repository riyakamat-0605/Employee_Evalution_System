def calculate_rating(tech, comm, prod):
    avg_score = (tech + comm + prod) / 3
    return avg_score, get_rating(avg_score)


def get_rating(avg_score):
    if avg_score >= 90:
        return "Outstanding"
    elif avg_score >= 80:
        return "Excellent"
    elif avg_score >= 65:
        return "Very Good"
    elif avg_score >= 50:
        return "Good"
    elif avg_score >= 40:
        return "Needs Improvement"
    else:
        return "Unsatisfactory"


if __name__ == "__main__":
    employee_name = "Riya"
    employee_id = 101
    department = "IT"

    technical_skills = 95
    communication = 90
    productivity = 92

    average_score, rating = calculate_rating(
        technical_skills, communication, productivity
    )

    print("Employee Performance Evaluation")
    print("-------------------------------")
    print("Employee Name:", employee_name)
    print("Employee ID:", employee_id)
    print("Department:", department)
    print("Average Score:", average_score)
    print("Rating:", rating)
