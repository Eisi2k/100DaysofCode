# 1st input: enter height in meters e.g: 1.65
height = input("Height: ")
# 2nd input: enter weight in kilograms e.g: 72
weight = input("Weight: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

numh = float(height)
numw = float(weight)
bmi = numw / (numh**2)
print(round(bmi))