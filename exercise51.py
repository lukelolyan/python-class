grade_points = {
    'A+': 4.0,
    'A': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1.0,
    'F': 0
}

user_grade = input("Enter your letter grade: ")

if user_grade in grade_points:
    print(f"The equivalent grade points for {user_grade} is: {grade_points[user_grade]}")
else:
    print("Invalid letter grade entered. Please enter a valid letter grade.")
