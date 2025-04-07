class Dog:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def sit(self):
        print(f"{self.name} is going to sit")

    def run(self):
        print(f"{self.name} is going to the dog park")


# Creating multiple Dog objects
dog1 = Dog("Buddy", "Golden Retriever", 3)
dog2 = Dog("Lucy", "Poodle", 5)
dog3 = Dog("Max", "German Shepherd", 2)
dog4 = Dog("Calvin", "yorkie", 3)

#Dog is the class.
#__init__ is the constructor method. It runs when you create a new Dog.
#self.name = name stores the dog's name.
#bark is a method, or function tied to the class.

#Class: blueprint
#Object: instance of a class
#Attributes: data stored in the object (like name)
#Methods: functions that operate on the object
# Using the bark method
dog1.bark()
dog2.bark()
dog3.bark()
dog4.sit()
dog4.run()

# Printing dog details
print(f"{dog1.name} is a {dog1.breed} aged {dog1.age}")
print(f"{dog2.name} is a {dog2.breed} aged {dog2.age}")
print(f"{dog3.name} is a {dog3.breed} aged {dog3.age}")
