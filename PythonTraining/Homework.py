# What is a Set?
# What is a Hashable Object
# What is Lambda
# What is Decorator
# Review List Comprehension
# Review Dictionary Comprehension
# What is functional programming?
# Is List and Array the same?
# What is the difference between an Argument and Parameter?

# Homework 1
"""
--- People:
Make two new dictionaries representing different people,
and store all three dictionaries in a list called people.
Loop through your list of people.
As you loop through the list, print everything you know about
each person.
--- Pets: Make several dictionaries,
where each dictionary represents a different pet.
In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets.
Next, loop through your list and as you do,
print everything you know about each pet.
---Favorite Places: Make a dictionary called favorite_places.
Think of three names to use as keys in the dictionary,
and store one to three favorite places for each person. T
o make this exercise a bit more interesting,
ask some friends to name a few of their favorite places.
Loop through the dictionary,
and print each person’s name and their favorite places.

"""
#“That function takes a sequence of numbers and returns the sum of those numbers.
# So if you were to invoke sum([1,2,3]), the result would be 6.”

# What does the "Splat" Operator do?

# This is a function - Difference between function and method
#

def mysum(*numbers): # this parameter should receive arguments,
# and that numbers will always be a tuple.
    output = 0
    for number in numbers:
        output += number
    return output


print(mysum(10, 20, 30, 40))

def greet(name):  # ← 'name' is a **parameter**
    print(f"Hello, {name}!")

greet("Alice")    # ← "Alice" is an **argument**
