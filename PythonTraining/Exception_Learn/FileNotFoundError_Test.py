from pathlib import Path

path = Path('programming.txt')
contents = path.read_text(encoding='utf-8')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    print()

