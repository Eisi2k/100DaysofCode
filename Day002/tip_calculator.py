#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What is the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip = tip / 100 * bill
bill_ges = tip + bill
final_amount = round(bill_ges / people, 2)
final_amount = "{:.2f}".format(final_amount) 


print(f"Each person should pay: ${final_amount}")