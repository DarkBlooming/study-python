class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def make_sound(self):
        print(f"{self.name} makes a sound!")

animal1 = Animal("Lucky", "Cat", 3)
animal2 = Animal("Astrid", "God", 8)

animal1.make_sound()
animal2.make_sound()
