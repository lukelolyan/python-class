def grade_point_to_letter_grade(grade_point):
    if grade_point >= 4.0:
        return 'A+'
    elif grade_point >= 3.7:
        return 'A-'
    elif grade_point >= 3.3:
        return 'B+'
    elif grade_point >= 3.0:
        return 'B'
    elif grade_point >= 2.7:
        return 'B-'
    elif grade_point >= 2.3:
        return 'C+'
    elif grade_point >= 2.0:
        return 'C'
    elif grade_point >= 1.7:
        return 'C-'
    elif grade_point >= 1.3:
        return 'D+'
    elif grade_point >= 1.0:
        return 'D'
    else:
        return 'F'

# User input for grade point value
grade_point = float(input("Enter the grade point value: "))
letter_grade = grade_point_to_letter_grade(grade_point)
print(f"The letter grade for {grade_point} is: {letter_grade}")
