"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random

def get_number(type):
    while True:
        bob = input(f"Enter a number for the {type}: ")
        try:
            return(int(bob))
        except ValueError:
            print("")


def dice_roll():
    total = 0
    for i in range(Count):
        rollval = random.randint(1, Type)
        print(f"Spin {i+1}: {rollval}")
        total = total + rollval

    print(f"Total of dice rolls == {total}")

while True:
    Type = get_number("side count of dice")
    Count = get_number("amount of dice rolled")
    dice_roll()
    bob = input("Do you want to run again? Y/N: ")
    if bob != "Y" and bob != "y":
        break
