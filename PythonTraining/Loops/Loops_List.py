testers = ['Sasha', 'Srini', 'Dave', 'Tek']
for x in testers:
    print(x)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")


print("Thank you, everyone. That was a great magic show!")


for value in range(1, 10):
    print(value)

squares = []
for value in range(1, 10):
    square = value ** 3
    squares.append(square)

print(squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

squares = [(value**2) * 12 for value in range(1, 11)]
print(squares)

cubes = [value**3 for value in range(1,5)]
print(cubes)

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:3])

# Slicing through a Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli','Sasha','Mike','Tek']
print("Here are the first three players on my team:")
for player in players[4:6]:
    print(player.title())

# Copying a List
learn_programs = ['Java', 'Python','Rust']
test_learn = learn_programs[:] # Use [:] to copy a list from one to another
print(learn_programs)
print(test_learn) # Verify if test_learn is same as learn_programs

# Now add new items to each list to verify that they are 2 new lists
learn_programs = ['Java', 'Python','Rust']
learn_programs.append('C++')
test_learn.append('Fortran')
print(learn_programs)
print(test_learn) # Verify if the two lists are different

# Homework test if you simply put test_learn = learn_programs does it produce two lists?
# Practice Slices and How it works?

# What is a Tuple? Python refers to values that cannot change as immutable,
# and an immutable list is called a tuple.

vector_num = (100, 200) # Tuple uses parentheses and not square brackets
print(vector_num[0])
print(vector_num[1])

# Try this code you will get a TypeError - As Tuple is immutable
#vector_num[0] = 75
#print(vector_num)
# You cannot modify a value in the tuple but you can assign new values to the variable
vector_num = (200, 400)
print(vector_num[0])
print(vector_num[1])
# what happens if you use the statement print(vector_num)? Try it

#Style Guide
# PEP 8 recommends that you use four spaces per indentation level.
# Using four spaces improves readability while leaving room for multiple levels of indentation on each line.
# Many Python programmers recommend that each line should be less than 80 characters.
# https://peps.python.org/pep-0008/


