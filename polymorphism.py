# Base class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        # Default implementation (optional, can be overridden)
        return f"{self.name} is moving."

# Child class: Fish
class Fish(Animal):
    def move(self):
        return f"{self.name} is swimming. 🐟"

# Child class: Bird
class Bird(Animal):
    def move(self):
        return f"{self.name} is flying. 🐦"

# Child class: Snake
class Snake(Animal):
    def move(self):
        return f"{self.name} is slithering. 🐍"

# Child class: Human
class Human(Animal):
    def move(self):
        return f"{self.name} is walking. 🚶‍♂️"

# Function to demonstrate polymorphism
def describe_movement(animal):
    print(animal.move())

# Create instances of each class
fish = Fish("Goldfish")
bird = Bird("Sparrow")
snake = Snake("Python")
human = Human("Alice")

# Call describe_movement for each instance
animals = [fish, bird, snake, human]
for animal in animals:
    describe_movement(animal)
