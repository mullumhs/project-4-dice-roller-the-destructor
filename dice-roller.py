"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
def convert(number):
    try:
        int(number)
        return(int(number))
    except ValueError:
         print("Value ERRORRR!!!")

def dice_roll():
    total = 0
    for i in range(convert(Count)):
        rollval = random.randint(1, convert(Type))
        print(f"Spin {i+1}: {rollval}")
        total = total + rollval

    print(f"Total of dice rolls == {total}")

while True:
    Type = input("Side count of dice: ")
    Count = input("Amount of dice rolled: ")

    dice_roll()
    bob = input("Do you want to run again? Y/N: ")
    if bob != "Y" and bob != "y":
        break
