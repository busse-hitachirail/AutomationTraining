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
