# Simple Employee Performance Evaluation Script for Jenkins without env vars

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

# Default values for Jenkins / non-interactive runs
DEFAULTS = {
    "EMP_NAME": "Riya Kamat",
    "EMP_ID": "1001",
    "DEPARTMENT": "IT",
    "TECH_SCORE": 95,
    "COMM_SCORE": 94,
    "PROD_SCORE": 89
}

def get_value(key, prompt, cast=str):
    try:
        # Try interactive input
        value = input(prompt)
        if value.strip() != "":
            return cast(value)
        else:
            raise EOFError
    except EOFError:
        # Non-interactive (Jenkins) or empty input: use default
        value = DEFAULTS[key]
        print(f"{prompt}{value} (default used)")
        return cast(value)

def main():
    # Collect all inputs
    name = get_value("EMP_NAME", "Enter employee name: ")
    emp_id = get_value("EMP_ID", "Enter employee ID: ")
    department = get_value("DEPARTMENT", "Enter department: ")

    tech = get_value("TECH_SCORE", "Technical score: ", int)
    comm = get_value("COMM_SCORE", "Communication score: ", int)
    prod = get_value("PROD_SCORE", "Productivity score: ", int)

    scores = [tech, comm, prod]
    rating = calculate_rating(scores)

    # Nicely aligned output
    print("\nEmployee Performance Evaluation")
    print("-" * 35)
    print(f"{'Name':15}: {name}")
    print(f"{'Employee ID':15}: {emp_id}")
    print(f"{'Department':15}: {department}")
    print(f"{'Technical':15}: {tech}")
    print(f"{'Communication':15}: {comm}")
    print(f"{'Productivity':15}: {prod}")
    print(f"{'Rating':15}: {rating}")

if __name__ == "__main__":
    main()
