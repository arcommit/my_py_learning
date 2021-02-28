student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for name, marks in student_scores.items():
    if 100 >= marks >= 91:
        student_grades[name] = "Outstanding"
    elif 90 >= marks >= 81:
        student_grades[name] = "Exceeds Expectations"
    elif 80 >= marks >= 71:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)
