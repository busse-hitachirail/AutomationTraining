#A dictionary in Python is a collection of key-value pairs.
# Each key is connected to a value, and you can use a
# key to access the value associated with that key.
# Dictionary is wrapped in curly braces

employee_data = {'age': 58, 'state': 'CA'}
print(employee_data['age'])
print(employee_data['state'])
naren_employee = employee_data['state']
print(f"Naren who is our employee lives in {naren_employee}")

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

"""students = {
 "101": {"name": "Alice", "age": 20, "grade": "A"},
   "102": {"name": "Bob", "age": 22, "grade": "B"},
"103": {"name": "Charlie", "age": 21, "grade": "A"},
}
#Fast lookup by key
print(students["101"]["name"])  # Output: Alice
# Adding a new student
students["104"] = {"name": "David", "age": 23, "grade": "B"}
# Removing a student
del students["102"]
"""

# Adding New Key-Value Pairs
employee_data = {'age': 58, 'state': 'CA'}
print(employee_data)
employee_data['city'] = 'sf'
employee_data['years'] = 3
print(employee_data)

# Adding to an Empty Dictionary. Use them for User Supplied Data
cars = {}
cars['color'] = 'blue'
cars['make'] = 'honda'
print(cars)

