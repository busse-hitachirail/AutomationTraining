#Inheritance allows one class to inherit attributes and methods from another,
# promoting code reuse


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow"

# Usage
dog = Dog("Buddy")
print(dog.name, "says", dog.speak())  # Output: Buddy says Bark
