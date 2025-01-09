# Base class: Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        return "Engine started!"

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"


# Child class: Car (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        # Use the parent class's constructor to set make, model, and year
        super().__init__(make, model, year)
        self.doors = doors  # Add a specific property for Car

    def start_engine(self):
        return f"{self.display_info()}: Car engine is starting!"

    def open_doors(self):
        return f"Opening {self.doors} doors."


# Child class: Motorcycle (inherits from Vehicle)
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, handlebar_type):
        # Use the parent class's constructor to set make, model, and year
        super().__init__(make, model, year)
        self.handlebar_type = handlebar_type  # Add a specific property for Motorcycle

    def start_engine(self):
        return f"{self.display_info()}: Motorcycle engine is starting!"

    def use_handlebars(self):
        return f"Using {self.handlebar_type} handlebars."


# Create instances of each class
vehicle = Vehicle("Generic", "ModelX", 2022)
car = Car("Toyota", "Corolla", 2020, 4)
motorcycle = Motorcycle("Harley-Davidson", "Iron 883", 2023, "standard")

# Test the methods
print(vehicle.display_info())
print(vehicle.start_engine())

print(car.display_info())
print(car.start_engine())
print(car.open_doors())

print(motorcycle.display_info())
print(motorcycle.start_engine())
print(motorcycle.use_handlebars())
