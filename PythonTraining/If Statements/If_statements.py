cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'audi':
        print(car.upper())
    else:
        print(car.title())

# At the heart of every if statement is an expression
# that can be evaluated as True or False and is called
# a conditional test.

car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'suzuki')

car = 'Honda'
print(car == 'honda')

car = 'Audi'
print(car.lower() == 'audi')
print(car)

type_test = 'manual'
if type_test != 'automation':  # Testing for inequality
    print("Need more automation test!")

age = 18
print(age == 18)

bob_age = 58
if bob_age != 42:
    print(f'{bob_age}, this is the right age.' )

age = 19
print(age < 21)
print(age <= 21)
print(age > 21)
print(age >= 21)


age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21)

age_1 = 21
print(age_0 >= 21 and age_1 >= 21)
print(age_0 >= 21 or age_1 >= 21)

name_planets = ['mercury', 'venus', 'earth']
print('earth' in name_planets)
print('moon' in name_planets)

testers_name = ['sasha', 'tek', 'alan']
manager = 'naren'

if manager not in testers_name:
    print(f"{manager.title()}, you are just a manager! not a great tester!" )

# Bottom line Boolean Expression is just another name for conditional test!!!

# If statements

age = 16
if age >= 18:
    print("You are old enough to vote")
    print("Please make sure you can vote")
    print("Make sure you vote")
else:
    print("You are not eligible to vote")

# If - elif - else
age = 45
if age < 4:
    print("Your ticket price is $4")
elif age < 18:
    print("Your ticket price is $25")
else:
    print("Your ticket price is $40")

# Another way to write it
age = 60
if age < 4:
    price = 5
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission price is ${price}")

# Multiple elif block

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"Your admission cost is ${price}.")


# Do you always need an else block at the end?
# Answer is no.
#The else block is a catchall statement.
# It matches any condition that wasn’t matched by a
# specific if or elif test, and that can sometimes
# include invalid or even malicious data.

# What to do when you have to test multiple conditions?
cars_buy = ['leather', 'Alarm']
if 'leather' in cars_buy:
    print("Would you like the leather Option?")
if 'GPS' in cars_buy:
    print("Would you like the GPS Option?")
if 'Alarm' in cars_buy:
    print('Would like the Alarm option?')

print('\nThe Car is available with your options')

# What will happen here? and why?
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

 # In summary, if you want only one block of code to run,
# use an if-elif-else chain.
# If more than one block of code needs to run,
# use a series of independent if statements.

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'pineapple':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

# Check if your list is empty
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_car_options = ['alarm','gps','leather','engine8']
requested_car_options = ['alarm','music','engine4']

for requested_car_option in requested_car_options:
    if requested_car_option in available_car_options:
        print(f"We have the following options {requested_car_option}")
    else:
        print(f"Sorry we dont have the following {requested_car_option}")

print("\nLet us know if you want car with your options")









