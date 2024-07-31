rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
print("Welcome to the Rock-Paper-Scissors Game!")
print("Get ready to challenge the computer.")
print("You can choose: Rock, Paper, or Scissors.")
print("Let's see if you can beat the machine!")
print("Good luck and have fun!")

while True:
    human = int(input("Please chooce Sissior , Paper, Rock or Quitt the game: (1-4) \n"))

    if human not in [1,2,3,4]:
        print("Invalid Input")
        break

    optionen = ["sissor", "paper", "rock"]
    if human == 4:
        break


    computer = random.choice([1,2,3])
    print(f"Your choice {optionen[human-1]}")
    print(f"Computer choose {optionen[computer-1]}")



    if human == computer:
        print(f"Draw you both took the same")
    elif (human == 1 and computer == 2 ) or (human == 2 and computer == 3) or (human == 3 and computer == 1):
        print("you win!")
    else:
        print("You loose!")

    more = input("Next game? Y/n\n")

    if more == "n":
        break
