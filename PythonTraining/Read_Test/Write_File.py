# Python can only write strings to a text file.
# If you want to store numerical data in a text file,
# you’ll have to convert the data to string format first using the str() function.


from pathlib import Path

path = Path('programming.txt')
path.write_text("I love programming.") # If the file that path points to doesn’t exist, it creates that file.
# Also, after writing the string to the file, it makes sure the file is closed properly.


from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents)

# Be careful when calling write_text() on a path object.
# If the file already exists, write_text() will erase the current contents of the file and write new contents to the file.

# HomeWork
# 10-4. Guest: Write a program that prompts the user for their name.
# When they respond, write their name to a file called guest.txt. 10-5. Guest Book:
# Write a while loop that prompts users for their name.
# Collect all the names that are entered, and then write these names to a file called guest_book.txt.
# Make sure each entry appears on a new line in the file.


