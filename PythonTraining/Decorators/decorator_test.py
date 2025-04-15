# Function One
def add_one(number):
    return number + 1
print(add_one(2))

#First-Class Objects
#In functional programming, you work almost entirely with pure functions that don’t have side effects.
#While not a purely functional language,Python supports many
# functional programming concepts, including treating functions as
# first-class objects.

# Function 2
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

def greet_bob(greeter_func):
    return greeter_func("Bob")

print(greet_bob(say_hello)) # This means that only a reference to the function is passed.
print(greet_bob(be_awesome))
# This is an important distinction that’s crucial for how functions work as first-class objects.
# A function name without parentheses is a reference to a function,
# while a function name with trailing parentheses calls the function and refers to its return value.

# Function 3 - Inner Functions
def parent():
    print("Printing from parent()")

    def first_child():
        print("Printing from first_child()")

    def second_child():
        print("Printing from second_child()")

    second_child()
    first_child()

parent()

# inner functions aren’t defined until the parent function is called.
# They’re locally scoped to parent(), meaning they only exist inside the parent() function as local variables
# Furthermore, the inner functions aren’t defined until the parent function is called. They’re locally scoped to parent(),
# meaning they only exist inside the parent() function as local variables. Try calling first_child(). You’ll get an error:

def parent(num):
    def first_child():
        return "Hi, I'm Bob"

    def second_child():
        return "Call me Jack"

    if num == 1:
        return first_child
    else:
        return second_child

first = parent(1)
second = parent(2)

print(type(first))
print(first())
print(second())
# If you call parent(), the inner functions first_child()
# and second_child() are also called.
# But because of their local scope,
# they aren’t available outside of the parent() function
# Python also allows you to return functions from functions

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = decorator(say_whee) # This is where the decoration happens.
#the name say_whee now points to the wrapper() inner function. Remember that you return wrapper as a function
# when you call decorator(say_whee)
print(say_whee)

# wrapper() has a reference to the original say_whee() as func, and it calls that function
# between the two calls to print()
# a decorator wraps a function, modifying its behavior







