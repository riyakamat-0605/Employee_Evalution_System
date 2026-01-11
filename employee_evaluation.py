import os
import sys

# -----------------------------
# Step 0: Override os.environ with command-line arguments
# Usage: python your_script.py EMP_NAME="John Doe" EMP_ID=1234 ...
for arg in sys.argv[1:]:
    if '=' in arg:
        key, value = arg.split('=', 1)
        os.environ[key] = value
# -----------------------------

def calculate_rating(scores):
    avg = sum(scores) / len(scores)

    if 90 <= avg <= 100:
        return "Outstanding"
    elif 80 <= avg < 90:
        return "Excellent"
    elif 65 <= avg < 80:
        return "Very Good"
    elif 50 <= avg < 65:
        return "Good"
    elif 40 <= avg < 50:
        return "Needs Improvement"
    else:
        return "Unsatisfactory"

def get_value(var, prompt, cast=str):
    # Use environment variable if it exists
    if var in os.environ:
        return cast(os.environ[var])
    
    # If running in an interactive terminal, ask the user
    try:
        return cast(input(prompt))
    except EOFError:
        # Non-interactive environment (like Jenkins), fallback to default
        print(f"{prompt} (no input, using default)")
        return cast("N/A" if cast == str else 0)

def collect_inputs():
    name = get_value("EMP_NAME", "Enter employee name: ")
    emp_id = get_value("EMP_ID", "Enter employee ID: ")
    department = get_value("DEPARTMENT", "Enter department: ")

    scores = [
        get_value("TECH_SCORE", "Technical score: ", int),
        get_value("COMM_SCORE", "Communication score: ", int),
        get_value("PROD_SCORE", "Productivity score: ", int),
    ]

    return name, emp_id, department, scores

def display_result(name, emp_id, department, rating):
    print("\nEmployee Performance Evaluation")
    print("-" * 31)
    print(f"Name        : {name}")
    print(f"Employee ID : {emp_id}")
    print(f"Department  : {department}")
    print(f"Rating      : {rating}")

if __name__ == "__main__":
    name, emp_id, department, scores = collect_inputs()
    rating = calculate_rating(scores)
    display_result(name, emp_id, department, rating)
