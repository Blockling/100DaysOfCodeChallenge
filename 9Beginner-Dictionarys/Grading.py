#Program that converts the student_scores scores into grades, judging each student by their score
student_scores = {
    "Harry"     : 81,
    "Ron"       : 78,
    "Hermione"  : 99,
    "Draco"     : 74,
    "Neville"   : 62,}
for student in student_scores:
    if student_scores[student] > 90:
        student_scores[student] = "Outstanding"
    elif student_scores[student] > 80:
        student_scores[student] = "Exceeds Expectations"
    elif student_scores[student] > 70:
        student_scores[student] = "Acceptable"
    else:
        student_scores[student] = "Failed"
print(student_scores)