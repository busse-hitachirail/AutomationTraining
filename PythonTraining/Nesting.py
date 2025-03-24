# Nesting Dictionary
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)


aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
    print("... ")
print(f"Total number of aliens: {len(aliens)}")
print()

for alien in aliens [0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien ['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


for alien in aliens[:5]:
    print(alien)
    print("...")

# Store information about a pizza being ordered.
pizza = {  # Create a dictionary
    'crust': 'thick', # Key 1
    'toppings': ['mushrooms', 'extra cheese'], # Key 2
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']} - crust pizza " # Break the statement up
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")


favorite_languages = {
    'sash': ['python', 'rust'],
    'tek': ['c'],
    'frank': ['rust', 'go'],
    'mike': ['python', 'haskell'],
    'alan': ["I love Brussels"]
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# Dictionary in Dictionary
users = {
    'franke': {
        'first': 'frank',
        'last': 'erkel',
        'location': 'pittsburgh',
        },

    'alany': {
        'first': 'alan',
        'last': 'younkin',
        'location': 'pittsburgh',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")



"""
--- People: Start with the program you wrote for Exercise 6-1 (page 98). 
Make two new dictionaries representing different people, 
and store all three dictionaries in a list called people. 
Loop through your list of people. 
As you loop through the list, print everything you know about 
each person. 
--- Pets: Make several dictionaries, 
where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the owner’s name. 
Store these dictionaries in a list called pets. 
Next, loop through your list and as you do, 
print everything you know about each pet. 
---Favorite Places: Make a dictionary called favorite_places. 
Think of three names to use as keys in the dictionary, 
and store one to three favorite places for each person. T
o make this exercise a bit more interesting, 
ask some friends to name a few of their favorite places. 
Loop through the dictionary, 
and print each person’s name and their favorite places. 




"""





