line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

x_value = ["A", "B", "C"]

if int(position[1]) == 1:
  line1[x_value.index(position[0])] = "X"
if int(position[1]) == 2:
  line2[x_value.index(position[0])] = "X"
if int(position[1]) == 3:
  line3[x_value.index(position[0])] = "X"

# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")