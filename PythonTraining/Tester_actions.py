class Tester:  # Class Names are Capitalized
    """This class defines what a tester does"""

    # 1) A function that’s part of a class is a method.
    # 2) The __init__() method is a special method that Python runs
    # 3) automatically whenever we create a new instance based on the Tester class.
    # 4) The self parameter is required in the method definition, and it must come first, before the other parameters
    # 5) Every method call associated with an instance automatically passes self,
    #    which is a reference to the instance itself; it gives the individual instance access to the attributes
    #    and methods in the class.



    def __init__(self, name, location):
        self.name = name # Any variable prefixed with self is available to every method in the class, and we’ll also be
        # able to access these variables through any instance created from the class.
        self.location = location

    def test_name(self):
        print(f"{self.name} is the tester's name and is a full time engineer.")

    def test_write(self):
        print(f"{self.name} is writing test cases and learning automation.")

# We are instantiating a class
tester_details = Tester('Alan', 'Pittsburg')
print(f"The tester on Australia project his name is {tester_details.name}") # Access attributes of an instance
print(f"Our tester is located in {tester_details.location}")

# We are calling the Methods
tester_details.test_name()
tester_details.test_write()