def count_up_to(max):
    count = 1
    while count <= max:
        print(f"Yielding {count}")
        yield count
        print(f"Resumed after yielding {count}")
        count += 1


for number in count_up_to(3):
    print(f"Received: {number}")

# What is the difference between Yield and Return
# Lazy Iterator
# Lazy and Memory Efficient
# Function will pause
# Use it for Large Datasets

