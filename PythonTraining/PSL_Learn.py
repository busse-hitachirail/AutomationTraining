#The Python standard library is a set of modules included with
# every Python installation.



from random import randint
from random import choice

test = randint(1, 100)
print(test)

testers = ['alan', 'tek', 'mike', 'mike b','tek']
first_choice = choice(testers).capitalize()
print(first_choice)

# Styling Classes
"""Styling Classes A few styling issues related to classes are worth clarifying, 
especially as your programs become more complicated. 
Class names should be written in CamelCase. 
To do this, capitalize the first letter of each word in the name, and don’t use underscores. 
Instance and module names should be written in lowercase, with underscores between words. 
Every class should have a docstring immediately following the class definition. 
The docstring should be a brief description of what the class does, 
and you should follow the same formatting conventions you used for writing docstrings in functions. 
Each module should also have a docstring describing what the classes in a module can be used for. 
You can use blank lines to organize code, but don’t use them excessively.
 Within a class you can use one blank line between methods, 
 and within a module you can use two blank lines to separate classes. 
 If you need to import a module from the standard library and a module that you wrote, 
 place the import statement for the standard library module first. 
 Then add a blank line and the import statement for the module you wrote. 
 In programs with multiple import statements, this convention makes it easier to see where the 
 different modules used in the program come from. 
 """