from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")

