class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def start_engine(self):
        return f"The car engine {self.display_info()} is running!"

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def rev_engine(self):
        return f"The motocycle engine {self.display_info()} is running!"

class Bicycle(Vehicle):
    def __init__(self, make, model, year, gear_count):
        super().__init__(make, model, year)
        self.gear_count = gear_count

    def ring_bell(self):
        return f"The ring bell {self.display_info()} is running!"

car = Car("Toyota", "Camry", 2020, "petrol")
motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2019, has_sidecar=False)
bicycle = Bicycle("Trek", "FX 3", 2021, gear_count=21)

print(car.display_info())
print(car.start_engine())

print(motorcycle.display_info())
print(motorcycle.rev_engine())

print(bicycle.display_info())
print(bicycle.ring_bell())
