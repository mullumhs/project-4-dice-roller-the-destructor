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
        return(number)
    except ValueError:
         print("Value ERRORRR!!!")

Type = input("Side count of dice: ")
Count = input("Amount of dice rolled: ")

def dice_roll():
