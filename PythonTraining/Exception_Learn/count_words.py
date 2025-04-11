from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')

    except FileNotFoundError:
        print(f"Sorry,the file {path} does not exist.")

    else:
        # Count the approximate number of words in the file:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")



filenames = ['programming.txt','programming2.txt',
             'programming3.txt','file_doesnot_exist']
for filename in filenames:
    path = Path(filename)
    count_words(path)




