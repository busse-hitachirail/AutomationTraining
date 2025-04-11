from pathlib import Path

def count_words(filename):
    try:
        contents = path.read_text(encoding='utf-8')

    except FileNotFoundError:
        print(f"Sorry,the file {path} does not exist.")

    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['programming.text','programming2.text',
             'programming3.text']
for filename in filenames:
    path = Path(filename)
    count_words(path)




