# 🚨 Don't change the code below 👇
# [180, 124, 165, 173, 189, 169, 146]
student_heights = input("Input a list of student heights ").split(',')
sum_height = 0
sum_students = 0
for n in range(0, len(student_heights)):
    sum_height += int(student_heights[n])

for student in student_heights:
    sum_students += 1

print(f"Total number of students = {sum_students} ")
print(f"Average height of a student = {round(sum_height/sum_students)} ")
# 🚨 Don't change the code above 👆




