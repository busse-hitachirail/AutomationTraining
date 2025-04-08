file_path = '/Users/narendraiyer/Desktop/Test1.txt'
word_to_count = 'python'

count = 0
with open(file_path, 'r') as file:
    for line in file:
        count += line.lower().count(word_to_count.lower())

print(f"The word '{word_to_count}' appears {count} times.")
