print(type(len))
test = "This is a word that can make a difference"
test_1 = ["This is a world"]
test_2 = {'first': 'alan', 'second' : "tek"}
print(len(test))
print(len(test_1))
print(len(test_2))

len = "This is a test"
print(type(len))
del len

print(type(len))
#“Because len is a built-in function name, it gets reassigned to the original function value.”
# How do you call a function - You have to use parentheses
# “An argument is a value that gets passed to the function as input.
# Some functions can be called with no arguments, and some can take as many arguments as you like.
# len() requires exactly one argument. and if you don't give it an argument you get this TypeError:
# len() takes exactly one argument (0 given)

numbers = len("Five")
print(numbers)

return_value = print("What do I return?")
print(type(return_value))
print(return_value)

#print() returns a special value called None that indicates the absence of data.
# None has a type called NoneType:
print("________________________________")
# Why do you write Functions? So you don't repeat yourself
# Function signature - Def is short for define - Function name is multiply
# The Parameter list and the Colon.
# When Python reads a line beginning with the def keyword,
# it creates a new function.
# The function is assigned to a variable with the same name as the function name.”
# Function Body
def greet():
    print("Hello!")
# Step 1: Define a function object
print(greet)       # <function greet at 0x...>
another = greet    # another points to the same function
another()          # prints "Hello!"

print("_________________________")

def multiply(x, y):
    """Returns the product of two numbers"""
    results = x*y
    return results # Function Stops Running
    print("this is a test")
print(multiply(2, 4))
help(multiply)

def testing(testtype):
    print(f"What type of, {testtype} testing are you doing?")
print(testing("BlackBox"))
print(help(len))

#“A container is a special name for an object
# that contains other objects.
# A string is a container because it contains characters.”
# Make sure indentation is done correctly - four spaces

print("----------------------------")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

c = 25
f = celsius_to_fahrenheit(c)
print(f"{c} C is equal to {f} F")

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32 ) * 5/9
    return celsius

f = 77
c = fahrenheit_to_celsius(f)
print(f"{f} F is equal to {c:.2f} C") #.2f is float with 2 decimals

# Positional Arguments
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='cat', pet_name='twinkle')


# Order Matters in Positional Arguments
# A keyword argument is a name-value pair
# that you pass to a function.

def describe_process(type_process, process='kanban'):
    """Display information about the process."""
    print(f"\nWe us the following {process}.")
    print(f"Our {type_process} process name is {process.title()}.")

print(describe_process(type_process='fast'))



