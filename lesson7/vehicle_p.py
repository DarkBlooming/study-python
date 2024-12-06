# Базовий клас
class Vehicle:
    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

    def display_info(self):
        print(f"This is {self.manufacturer} {self.model} {self.year} year of manufacture.")

class Car(Vehicle):
    def __init__(self, manufacturer, model, year, doors):
        super().__init__(manufacturer, model, year)
        self.doors = doors

    def display_info(self):
        print(f"This car is {self.manufacturer} {self.model} {self.year} year of manufacture and has {self.doors} doors.")

class Motorcycle(Vehicle):
    def __init__(self, manufacturer, model, year, engine_type):
        super().__init__(manufacturer, model, year)
        self.engine_type = engine_type

    def display_info(self):
        print(f"This motocycle is {self.manufacturer} {self.model} {self.year} year of manufacture with an engine of the type {self.engine_type}.")

class Truck(Vehicle):
    def __init__(self, manufacturer, model, year, max_load):
        super().__init__(manufacturer, model, year)
        self.max_load = max_load

    def display_info(self):
        print(f"This truck is {self.manufacturer} {self.model} {self.year} year of manufacture. It can carry up to {self.max_load} tonnes.")

vehicles = [
    Car("Toyota", "Corolla", 2020, 4),
    Motorcycle("Yamaha", "R1", 2019, "sports engine"),
    Truck("Volvo", "FH16", 2022, 25)
]

for vehicle in vehicles:
    vehicle.display_info()
