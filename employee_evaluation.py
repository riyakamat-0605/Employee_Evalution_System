import os

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
    # Use Jenkins environment variable if set
    if var in os.environ and os.environ[var].strip() != "":
        value = os.environ[var]
        print(f"{prompt}{value} (from environment)")
        return cast(value)
    
    # Else, ask user for input
    value = input(prompt)
    return cast(value)

def main():
    name = get_value("EMP_NAME", "Enter employee name: ")
    emp_id = get_value("EMP_ID", "Enter employee ID: ")
    department = get_value("DEPARTMENT", "Enter department: ")

    tech = get_value("TECH_SCORE", "Technical score: ", int)
    comm = get_value("COMM_SCORE", "Communication score: ", int)
    prod = get_value("PROD_SCORE", "Productivity score: ", int)

    scores = [tech, comm, prod]
    rating = calculate_rating(scores)

    print("\nEmployee Performance Evaluation")
    print("-" * 35)
    print(f"Name         : {name}")
    print(f"Employee ID  : {emp_id}")
    print(f"Department   : {department}")
    print(f"Technical    : {tech}")
    print(f"Communication: {comm}")
    print(f"Productivity : {prod}")
    print(f"Rating       : {rating}")

if __name__ == "__main__":
    main()
