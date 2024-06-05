class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("drive")
class plane:
    def __init__(self,brand,model):
        return
    def move(self):
        print("fly")

car1=car("audi","german")
plane1=plane("airways","kenya")
for x in (car1 ,plane1):
    x.move()

































class Animal:
    def __init__(self,name):
        self.name=name
    def move(self):
        print(f"{self.name} is moving")
class Cow(Animal):
    def move(self):
        print("walking")
class Bird(Animal):
    def move(self):
        print("flying")
class Donkey(Animal):
    pass
Freshian=Cow("marcy")
eagle=Bird("henry")
donkey1=Donkey("Max")
Freshian.move()
eagle.move()
donkey1.move()
