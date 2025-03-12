"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                GUESSING GAME
---------------------------------------------------------------------------------
- File Name: dice-roller.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Complete a functional dice roller app in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
import random
def get_number(number):
    try:
        int(number)
        return(int(number))
    except ValueError:
         print("Value ERRORRR!!!")

Type = input("Side count of dice: ")
Count = input("Amount of dice rolled: ")

def dice_roll():
    total = 0
    for i in range(get_number(Count)):
        rollval = random.randint(1, get_number(Type))
        print(f"Spin {i+1}: {rollval}")
        total = total + rollval

    print(f"Total of dice rolls == {total}")
dice_roll()