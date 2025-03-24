# Input

name = input("Please enter your name: ")
print(f"\nHello, {name}!")
# Using a multiline String
prompt = "If you share your favorite project, we can give you a message!"
prompt += "\nWhat is your favorite project? "
project = input(prompt)
print(f"\n{name}, the {project} project!, met the scrum standards and 95% efficiency"
      f"for last three years!")
print("________________________")

#Using int() to Accept Numerical Input Fixing it by adding int
#TypeError: '>=' not supported between instances of 'str' and 'int'
years = input("How many years have you been at Hitachi?")
years = int(years)
if years >= 5:
    print("What an experienced engineer!")
else:
    print("Still have a lot to learn")

print("________________________")
# What is a Modulo Operator? Tells you what the remainder is
x = 6 % 3
print(x)

print("________________________")
# Simple Example of Even and Odd.
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
print("________________________")
# Homework
"""
Rental Car: Write a program that asks the user what kind of rental car they would like. 
Print a message about that car, such as “Let me see if I can find you a Subaru.”
"""

# The for loop takes a collection of items and executes a block of code once for each item in the collection.
# In contrast, the while loop runs as long as, or while, a certain condition is true.

# Sample Code
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 #(The += operator is shorthand for current_number = current_number + 1.)
print("________________________")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

print("________________________")

# Using a break statement
prompt = "\nPlease enter the name of managers you have reported to:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True: # This loop will run forever!
    manager = input(prompt)

    if manager == 'quit':
        break
    else:
        print(f"I'd reported to  {manager.title()}!")
print('________________________________')

# Use Continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
print('________________________________')


# Infinite Loop - Fix this Infinite Loop
# This loop runs forever!
"""x = 1
while x <= 5:
    print(x) """

# Setting a Flag
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)


T

# Homework
"""Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. 
If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; 
and if they are over age 12, the ticket is $15. 
Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.
Use a conditional test in the while statement to stop the loop. 
Use an active variable to control how long the loop runs. 
Use a break statement to exit the loop when the user enters a 'quit' value.
"""





