"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
                                    LAB 2
---------------------------------------------------------------------------------
- File Name: lab2.py
- Teacher: David Steedman
- Class: Software Engineering
- Description: Create and use functions with parameters in Python
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Create a function named say_hello that accepts a person's name as a parameter and prints "Hello" followed by the name.
def say_hello(name):
    print(f"Hello {name}")

# Develop a function named triple that takes one number as a parameter and returns the number multiplied by three.
def triple(number):
    try:
        float(number)
        number1 = float(number)
        print(number1 * 3)
    except ValueError:
         print("Incorrect parameter")
    

    

# Write a function called add that takes two numbers as parameters and returns their sum. 
def add(num1, num2):
    try:
        float(num1)
        numb1 = float(num1)
        float(num2)
        numb2 = float(num2)
        print(numb1 + numb2)

    except ValueError:
         print("Incorrect parameter")
    
# Create a function named draw_line that takes one parameter for the length of the line and prints a straight line of that many hyphens.
def draw_line(length):
    try:
        int(length)
        lengthnum = int(length)
        print("-"*lengthnum)
    except ValueError:
        print("Incorrect parameter")
    

# Call your functions, printing out the return result where appropriate
say_hello("kane")
triple(2)
add(2, "a")
draw_line(12)