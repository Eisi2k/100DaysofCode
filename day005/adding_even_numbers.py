target = int(input("Please number: ")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

total = 0

for number in range(1,target+1, 1):
  if number%2 == 0:
    total += number

print(total)