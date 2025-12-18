#Grading system
def grade_system(marks):
    if marks >= 90:
        return "Excellent"
    elif marks <= 80 or marks >70:
        return " Good job"
    elif marks <= 70 or marks > 50:
        return "Average"
    elif marks <= 50 and marks >= 0:
        return "Needs improvement"
    else:
        return "Invalid marks"


