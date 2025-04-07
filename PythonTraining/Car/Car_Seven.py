#If the class you’re writing is a specialized version of another class
# you wrote, you can use inheritance.
# When one class inherits from another, it takes on the attributes and
# methods of the first class.
# The original class is called the parent class,
# and the new class is the child class.
# The child class can inherit any or all of the
# attributes and methods of its parent class,
# but it’s also free to define new attributes and methods of its own.
# The __init__() Method for a Child Class
# call the __init__() method from the parent class.
# This will initialize any attributes that were defined in the
# parent __init__() method and make them available in the child class.


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
            """Print a statement showing the car's mileage."""
            print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) #The super() function
        # is a special function that allows you to call a method
        # from the parent class.
        #The name super comes from a convention of calling the
        # parent class a superclass and the child class a subclass.




my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())










