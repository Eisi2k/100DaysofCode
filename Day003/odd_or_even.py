# Which number do you want to check?
number = int(input("Check if odd or even: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
num = number % 2
if num == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")