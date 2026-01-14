# Program to calculate employee performance rating
import sys

def calculate_average(s1, s2, s3):
    return (s1 + s2 + s3) / 3

def assign_rating(avg):
    if avg >= 90:
        return "Outstanding"
    elif avg >= 80:
        return "Excellent"
    elif avg >= 65:
        return "Very Good"
    elif avg >= 50:
        return "Good"
    elif avg >= 40:
        return "Needs Improvement"
    else:
        return "Unsatisfactory"

if __name__ == "__main__":
    print("=== Employee Performance Evaluation System ===")

    try:
        if len(sys.argv) == 7:
            name = sys.argv[1]
            emp_id = sys.argv[2]
            department = sys.argv[3]
            s1 = float(sys.argv[4])
            s2 = float(sys.argv[5])
            s3 = float(sys.argv[6])
        else:
            name = input("Enter Employee Name: ")
            emp_id = input("Enter Employee ID: ")
            department = input("Enter Department: ")
            s1 = float(input("Enter Technical Skills Score: "))
            s2 = float(input("Enter Communication Score: "))
            s3 = float(input("Enter Productivity Score: "))

        print("\nEmployee Details")
        print("Name:", name)
        print("Employee ID:", emp_id)
        print("Department:", department)
        print("Scores:", s1, s2, s3)

        avg = calculate_average(s1, s2, s3)
        rating = assign_rating(avg)

        print("\nAverage Score:", avg)
        print("Performance Rating:", rating)

    except ValueError:
        print("Invalid input")
