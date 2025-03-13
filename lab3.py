"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 3
---------------------------------------------------------------------------------
- File Name: lab3.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Learn how to use exception handling in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Define a function called get_number(prompt) that returns an integer. 
# Include a while loop and try/except blocks inside the function to handle non-integer inputs.
def convert_int(number):
    try:
        int(number)
        return(int(number))
    except ValueError:
         print("Value ERRORRR!!!")

def get_number():
    while True:
        bob = input("Enter a whole number: ")
        try:
            return(int(bob))
        except ValueError:
            print("Value ERRORRR!!!")


# Use the get_number function to ask for a numerator, then again for a denominator.
# Divide the numerator by the denominator and print the result, handling any division by zero errors.
def division(numerator, denominator):  
    
    try:
        bob = convert_int(numerator) / convert_int(denominator)
        print(bob)
    except ZeroDivisionError:
        print("You can't divide by ZERO!!")



# Use the get_number function to ask the user for an index to access an element from a predefined list. 
# Print out the value from the list, handling the index error if the user selects a non-existent index.
def list(index):
    list = division(1, 1478), "transparent", "shade", "black", "red", "linc_colour", "light"
    try:
        print(list[convert_int(index)])
    except IndexError:
         print("Number isn't in the list")


division(get_number(), get_number())
list(get_number())