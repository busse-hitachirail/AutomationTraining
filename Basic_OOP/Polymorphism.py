# Polymorphism allows different classes to have methods with the same name b
# ut different behaviors

class Bird:
    def speak(self):
        return "Chirp"

class Horse:
    def speak(self):
        return "Neigh"

# Polymorphic function
def animal_sound(animal):
    print(animal.speak())

bird = Bird()
horse = Horse()

animal_sound(bird)  # Output: Chirp
animal_sound(horse) # Output: Neigh
