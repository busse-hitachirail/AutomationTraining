print(type(len))
test = "This is a word that can make a difference"
test_1 = ["This is a world"]
test_2 = {'first': 'alan'}
print(len(test))
print(len(test_1))
print(len(test_2))

len = "This is a test"
print(type(len))
del len
print(type(len))
# Because len is a built-in function name, it gets reassigned to the original function value.

# How do you call a function - You have to use parentheses
# An argument is a value that gets passed to the function as input.
# Some functions can be called with no arguments, and some can take as many arguments as you like.
# len() requires exactly one argument. and if you don't give it an argument you get this TypeError:
# len() takes exactly one argument (0 given)
numbers = len("Five")
print(numbers)


return_value = print("What do I return?")
print(type(return_value)) # What happens when a variable has no value
print(return_value)

#print() returns a special value called None that indicates the absence of data.
# None has a type called NoneType:
print("________________________________")
# Why do you write Functions? So you don't repeat yourself
# Function signature - Def is short for define - Function name is multiply
# The Parameter list and the Colon.
# When Python reads a line beginning with the def keyword,
# it creates a new function.
# The function is assigned to a variable with the same name as the function name
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
    # Function Body
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
    print(f"My {animal_type}'s name is {pet_name.capitalize()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(animal_type='cat', pet_name='ryzhik')


# Order Matters in Positional Arguments
# A keyword argument is a name-value pair
# that you pass to a function.

def describe_process(type_process, process='kanban'):
    """Display information about the process."""
    print(f"\nWe use the following {process}.")
    print(f"Our {type_process} process name is {process.title()}.")
print(describe_process(type_process='fast'))

# Return Values
# The value the function returns is called a return value.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

manager = get_formatted_name('Frank', 'erkel')
print(manager)

# Python interprets non-empty strings as True,
def get_formatted_name(first_name,last_name, middle_name =''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}" #If no middle name is provided,
        # the empty string fails the, if test and the else block runs
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('freddie', 'mercury')
print(musician)

musician = get_formatted_name('taylor', 'allison', 'swift')
print(musician)

def build_name(first_name, last_name):
    """Return a dictionary about a name"""
    person = {"first": first_name, 'last': last_name}
    return person

build_manager = build_name('super','man')
print(build_manager)

# special value None, which is used when a variable has no specific value assigned to it.
# Think of None as a placeholder value.


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('david', 'bowie', age=65)
print(musician)


def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)


usernames = ['alan', 'tek', 'mikeB','mike','sasha']
greet_users(usernames)

# Modifying a List in a Function


testers_australia = ['tek', 'alan', 'mike']
budget = []


while testers_australia:
    current_wbs= testers_australia.pop()
    print(f"testers learning: {current_wbs}")
    budget.append(current_wbs)

# Display all completed models.
print("\nThe following testers are on current wbs:")
for tester in budget:
    print(tester)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

def australia_tester(testers_australia,budget):
    """Printing the name of the testers"""
    while testers_australia:
        current_wbs = testers_australia.pop()
        print(f"testers learning: {current_wbs.lower()}")
        budget.append(current_wbs)

def show_names(budget):
    print("\nThe following testers are on current wbs:")
    for tester in budget:
        print(tester.upper())


testers_australia = ['tek', 'alan', 'mike','sasha']
budget = []

australia_tester(testers_australia,budget)
show_names(budget)

# Passing an Arbitrary Number of Arguments

def name_tester(*names):# Tells Python to make a tuple
    """Print the list of tester names that have been requested."""
    print(names)

name_tester('alan')
name_tester('mallesh', 'srini', 'doug','sasha')

def name_tester(*names):
    print("\nHere are the following testers available:")
    for name in names:
        print(f"-{name}")


name_tester('alan')
name_tester('sasha','mike','tek')


def name_tester(type_test,*names):
    print(f"\nWe will do {type_test} testing with following testers:")
    for name in names:
        print(f"-{name}")

name_tester('black_box', 'alan','naren')
name_tester('white box', 'sasha')
name_tester('automation', 'tek','mike')

"--------------"

def tester_profile(first, last, **user_info): # **user_info cause Python to create a dictionary called user_info.

    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = tester_profile('frank', 'erkel',
                             location='pittsburgh',
                             field='testing')
print(user_profile)




