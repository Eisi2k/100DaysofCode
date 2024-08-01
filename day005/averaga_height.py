# Input a Python list of student heights
student_heights = [123, 565, 766]
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
height = 0
counter = 0

for student in student_heights:
  height += student
  counter += 1

print(f"total height = {height}")
print(f"number of students = {counter}")
print(f"average height = {round(height/counter)}")