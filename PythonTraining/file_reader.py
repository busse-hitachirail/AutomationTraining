from pathlib import Path
path = Path('pi_digits.txt') # Python provides a module called pathlib that makes it easier to work with files
contents = path.read_text()
contents = contents.rstrip()
print(contents)