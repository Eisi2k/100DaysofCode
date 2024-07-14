print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
name1 = name1 + name2
count_true = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
count_love = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
love = int(str(count_true) + str(count_love))

if love < 10 or love > 90:
  print(f"Your score is {love}, you go together like coke and mentos.")
elif 40 < love < 50:
  print(f"Your score is {love}, you are alright together.")
else:
 print(f"Your score is {love}.")
