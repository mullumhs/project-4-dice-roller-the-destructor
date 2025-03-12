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
def get_number(number):
    try:
        int(number)
        return(number)
    except ValueError:
         print("Value ERRORRR!!!")

    


# Use the get_number function to ask for a numerator, then again for a denominator.
# Divide the numerator by the denominator and print the result, handling any division by zero errors.
def division(numerator, denominator):  
    
    try:
        bob = get_number(numerator) / get_number(denominator)
        print(bob)
    except ZeroDivisionError:
        print("You can't divide by ZERO!!")



# Use the get_number function to ask the user for an index to access an element from a predefined list. 
# Print out the value from the list, handling the index error if the user selects a non-existent index.
def list(index):
    list = "clear", "transparent", "shade", "black", "red", "linc_colour", "light"
    index1 = get_number(index)
    try:
        print(list[index1])
    except IndexError:
         print("Number isn't in the list")


division(1, 3)
list(2)