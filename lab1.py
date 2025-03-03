"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 1
---------------------------------------------------------------------------------
- File Name: lab1.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Write a function named welcome_message that prints out "Welcome to our program!" whenever it is called.
def penisfunction():
    print ("Welcome to kane and jaali programn")


# Create a function named print_divider that prints out a line of asterisks (e.g., "**********") to act as a section divider.
def ballsfunction():
    print("*" *100)


# Write a function named get_number that asks the user to input a whole number and then returns the result as an integer.
def bigmnafunction():
    bob = False
    x = input("Input a whole number: ")
    while bob == False:
        try:
            int(x)
            bob = True
            return int(x)
            
        except ValueError:
            bob = False
            x = input("Input a whole number: ")



# Create a function named get_random_colour that, when called, returns a random colour from a predefined list of colours.
import random
def jaalilovefunction():
    x = random.randint(1, 7)
    colours = "clear", "transparent", "shade", "black", "red", "linc_colour", "light"
    return colours[x]



# Call all of your functions to demonstrate that they work
penisfunction()
ballsfunction()
print(bigmnafunction())
print(jaalilovefunction())