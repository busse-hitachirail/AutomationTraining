#What is Inheritance in Python?
# Inheritance allows one class (called the child or subclass)
# to inherit attributes and methods from another class
# (called the parent or superclass).

# Example
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("Dog barks")

d = Dog()
d.speak()  # Inherited from Animal
d.bark()   # Defined in Dog

class ElectricCar(Car):
    """Use Code"""

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

 