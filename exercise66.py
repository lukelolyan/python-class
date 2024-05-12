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

grades = []
while True:
    grade = input("Enter a letter grade (or press Enter to calculate GPA): ")
    if grade == '':
        break
    grades.append(grade)

total_points = sum(grade_points[grade] for grade in grades)
gpa = total_points / len(grades) if len(grades) > 0 else 0

print(f"The Grade Point Average (GPA) is: {gpa}")
