class Dog:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Dog's name is: {self.name}")

class Labrador(Dog): #single inheritance
    def sound(self):
        print("Labrador woofs")
    
class GuideDog(Labrador): #multilevel inheritance
    def guide(self):
        print(f"{self.name}Guides the way!")

class Friendly:
    def greet(self):
        print("Friendly")

class GoldenRetrieever(Dog, Friendly): #multiple inheritance
    def sound(self):
        print("Golden Retriever barks")


lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide = GuideDog("Max")
guide.display_name()
guide.sound()

retriever = GoldenRetrieever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()

class Animal:
    def __init__():
        print("Animal Created")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Cat's name is: {self.name}")

class Dog(Animal): #Hierarchical inheritance
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Dog's name is: {self.name}")

cat = Cat("Whiskers")
cat.display()

dog = Dog("Rex")
dog.display()

class Lion: #Hybrid inheritance
    def roar(self):
        print("Lion roars")

class Tiger(Lion):
    def growl(self):
        print("Tiger growls")

class Liger(Tiger, Dog):
    def display(self):
        print(f"Liger's name is: {self.name}")

liger = Liger("Leo")
liger.display()
liger.roar()
liger.growl()


class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stopped")

class ToyotoCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotoCar("Fortuner", "Electric")

print(car1.name)
print(car1.type)

#Class Method Decorator
class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Alice")
print(p1.name)
print(Person.name)