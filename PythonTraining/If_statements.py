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
