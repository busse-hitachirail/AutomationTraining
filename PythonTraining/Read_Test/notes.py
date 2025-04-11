# A relative file path tells Python to look for a given location relative to the directory where the currently running program file is stored.
# Since text_files is inside python_work, we need to build a path that starts with the directory text_files, and ends with the filename.
# Here’s how to build this path:
# Relative Path = Path('text_files/filename.txt')

# Python exactly where the file is on your computer, regardless of where the program that’s being executed is stored.
# This is called an absolute file path.
# Absolute Path = Path('/home/naren/data_files/text_files/filename.txt')

# Note Windows systems use a backslash (\) instead of a forward slash (/)
# when displaying file paths, but you should use forward slashes in your code, even on Windows.
# The pathlib library will automatically use the correct representation of the path
# when it interacts with your system, or any user’s system.

# import os

#In the case of reading from a file, quite often the file
# needs to be open only one time: while data is being read.
# Then the file can be close
# Context Managers
# Context managers are great for things like locking and unlocking resources, closing files,
# committing database transactions, and so on
#Python’s philosophy is that errors shouldn’t pass silently unless they’re explicitly silenced.
"""Python’s exception-handling mechanism and exception classes provide a rich system to handle runtime errors in your code.
Python exception types are organized in a hierarchy because exceptions, like all objects in Python, are classes.
By using try, except, else, and finally blocks, and by selecting and even creating the types of exceptions caught,
you can have very fine-grained control over how exceptions are handled and ignored.
You can define a new exception by inheriting (preferably) from Exception.
Exceptions can be conditionally raised by using an assert statement.
Invoking a context manager by using the with keyword can ensure actions even if an exception occurs, as in reading or writing a file.

You can easily define your own exception. The following two lines do this for you:
class MyError(Exception):
    pass
raise MyError("Some information about what went wrong")
This code creates a class that inherits everything from the base Exception class.
But you don’t have to worry about that if you don’t want to.
You can raise, catch, and handle this exception like any other exception.
If you give it a single argument (and you don’t catch and handle it),
it’s printed at the end of the traceback:"""


