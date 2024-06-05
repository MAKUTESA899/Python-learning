class Animal:
    def make_sound(self):
        raise NotImplementedError("subclasses should implement this method!")
class Dog(Animal):
    def make_sound(self):
        return "woof"
class cat(Animal):
    def make_sound(self):
        return "Meow"
class cow(Animal):
    def make_sound(self):
        return "moo"

def animal_sound(animal):
    for animal in animals:
        print(animal.make_sound())

animals=[Dog(), cat(), cow()]
animal_sound(animals)
