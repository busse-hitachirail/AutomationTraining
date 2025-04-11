from pathlib import Path

path = Path('programming.txt')
contents = path.read_text(encoding='utf-8')

words = contents.split()
num_words = len(words)
print(f"The file {path} has about {num_words} words.")

