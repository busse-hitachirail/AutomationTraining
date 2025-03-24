#A dictionary in Python is a collection of key-value pairs.
# Each key is connected to a value, and you can use a
# key to access the value associated with that key.
# Dictionary is wrapped in curly braces


employee_data = {'age': 21, 'state': 'PA'}
print(employee_data['age'])
print(employee_data['state'])
sasha_employee = employee_data['state']
print(f"Sasha, who is our employee lives in {sasha_employee}")

# A key’s value can be a number,
# a string, a list, or even another dictionary.
# In fact, you can use any object that you can create in Python
# as a value in a dictionary.

color_shirt = {'color': 'green'}
# Color is the Key
# Green is the Value
# Key-Value Pair
# Dictionaries  are called Dynamic Structures. They are good for fast lookups
# Lists and Tuples are best for ordered sequences
# A dictionary is useful when you need to associate keys (unique identifiers)
# with values (data)

students = {
 "101": {"name": "Alice", "age": 20, "grade": "A"},
 "102": {"name": "Bob", "age": 22, "grade": "B"},
 "103": {"name": "Charlie", "age": 21, "grade": "A"},
}
# Fast lookup by key
print(students["101"]["name"])  # Output: Alice
# Adding a new student
students["104"] = {"name": "David", "age": 23, "grade": "B"}
# Removing a student
del students["102"]


# Adding New Key-Value Pairs
employee_data = {'age': 58, 'state': 'CA'}
print(employee_data)
employee_data['city'] = 'sf'
employee_data['years'] = 3
employee_data['social'] = 3165
employee_data['address'] = 1024
employee_data['insurance'] = "Blue Cross"
print(employee_data)

# Adding to an Empty Dictionary. Use them for User Supplied Data
cars = {}
cars['color'] = 'silver'
cars['make'] = 'subaru'
cars['year'] = 2017
print(cars)

print(f"Tek has a {cars['color']} and the make of the car is {cars['make']} and the year is {cars['year']}, but he rather buy a Tesla!")

# Modify Values in Dictionary
cars['color'] = 'black'
cars['make'] = 'subaru'
cars['year'] = 2024
print(cars)

print(f"Tek has a {cars['color']} and the make of the car is {cars['make']} and the year is {cars['year']}, but he rather buy a Tesla!")
print()

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
 x_increment = 1
elif alien_0['speed'] == 'medium':
 x_increment = 2
else:
 # This must be a fast alien.
 x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
print()

programming_language = {
    'sasha': 'rust',
    'tek' : 'java',
    'mike' : 'python',
    'alan' : 'python'
}
testers = ['alan', 'sasha']
language = programming_language['sasha'].title()
print(f"Sasha's favorite language is {language}")
print()

for name, language in programming_language.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
print()
print()

for name in programming_language.keys():
    print(f" Hi {name.title()}.")

    if name in testers:
     language = programming_language[name].title()
     print(f"\t{name.title()}, I see you love {language}!")
     print()

    if 'naren' not in programming_language.keys():
        print("Naren can you fill out the survey")
    print()

    for name in sorted(programming_language.keys()):
     print(f"{name.title()}, thank you for taking the poll.")
     print()

    print("The following languages have been mentioned:")
    for language in programming_language.values():
     print(language.title())
     print()

    print("The following languages have been mentioned:")
    for language in set(programming_language.values()):
     print(language.title())
     print()

    pr_languages = languages = {'c++', 'python', 'c', 'python'}
    print(pr_languages)

# HomeWork
"""
Rivers: Make a dictionary containing three major rivers 
and the country each river runs through. 
One key-value pair might be 'nile': 'egypt'. 
Use a loop to print a sentence about each river, 
such as The Nile runs through Egypt. 
Use a loop to print the name of each river included in the dictionary. 
Use a loop to print the name of each country included in the dictionary.
"""

train_details = {'track': 10, 'speed':'slow'}
train_name = train_details.get('name', 'no name assigned' )
#print(train_details)
print(train_name)

country_name = {
    'name' : 'washington dc',
    'states' : 50,
    'bird' : 'bald eagle'
}
# Rewrite it as a Set

for key, value in country_name.items(): #items returns sequence for key-value pairs
    print(f"\nKey: {key.title()}") # \n insert bland line
    print(f"Value: {value}")
    print()
    print()


# Alan and Tek will fix this Code.
testers = []
for tester in testers :
    automation_tester = {'programming': 'python', 'experience': 3, 'state': 'USA'}
    testers.append(automation_tester)
for tester in testers[:10]:
    print()
print(f"Total number of testers: {len(testers)}")











