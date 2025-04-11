from pathlib import Path
path = Path('pi_digits.txt') # Python provides a module called pathlib that makes it easier to work with files
contents = path.read_text()
contents = contents.rstrip()
print(contents)

path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines() # splitlines() is a string method used to split a string into a list of lines
for line in lines:
    print(line)