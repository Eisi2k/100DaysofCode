
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

import os
import time

def clear_screen():
    os.system('cls')

def print_delayed(text, delay=0.5):
    print(text)
    time.sleep(delay)

def play_game():
    clear_screen()
    print("Welcome to Treasure Island. Your mission is to find the treasure")
    time.sleep(0.5)

    print("You are standing at a crossroads on a mysterious island. Where do you want to go?")
    choice = input("Left or Right? ").lower()

    clear_screen()

    if choice == "left":
        print_delayed("You walk down a narrow path and hear the sound of a river.")
        print_delayed("After making your decision, you encounter a river.")
        choice = input("Do you want to swim or wait? ").lower()

        clear_screen()

        if choice == "wait":
            print_delayed("You wait patiently on the shore, and after a while, a small boat appears to take you safely across.")
            print_delayed("You reach an ancient castle with three doors: one red, one blue, and one yellow.")
            choice = input("Which door do you choose? ").lower()

            clear_screen()

            if choice == "red":
                print_delayed("Behind the red door, you find a room full of fire. Unfortunately, you are burned alive.")
                print_delayed("Game Over: You were burned alive.")
            elif choice == "blue":
                print_delayed("The blue door leads to a room full of wild animals that immediately rush at you. You are eaten by the animals.")
                print_delayed("Game Over: You were eaten by wild animals.")
            elif choice == "yellow":
                print_delayed("The yellow door opens to a room filled with gold and jewels. You have found the treasure and win!")
                print_delayed("Congratulations: You found the treasure!")
            else:
                print_delayed("Invalid choice. Game Over.")

        else:
            print_delayed("You jump into the water and start swimming, but the current is strong and pulls you away. Unfortunately, you drown.")
            print_delayed("Game Over: You drowned.")

    else:
        print_delayed("The path leads you through a dense jungle, where you suddenly fall into a hidden trap and die.")
        print_delayed("Game Over: You died!")

while True:
    play_game()
    replay = input("Do you want to play again? (yes or no): ").lower()
    if replay != "yes":
        print("Thanks for playing! Goodbye.")
        break
