class Dog:
    species = "Dog" #class attribute

    def __init__(self, name, age):
        self.name = name #instance attribute
        self.age = age

obj1 = Dog("Buddy", 3)
print(obj1.name, obj1.age, obj1.species)
obj1.name = "Max" #modifying instance attribute
# obj1.species = "Wolf" #creating new instance attribute
print(obj1.species)
print(obj1.name)

obj2 = Dog("Lucy", "5")
print(obj2.name, obj2.age, obj2.species)

Dog.species = "Canine" #modifying class attribute
print(obj1.species)
print(obj2.species)

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no #public attribute
        self.__acc_pass = acc_pass #private attribute
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12335", "abcde")
print(acc1.acc_no)
# print(acc1.__acc_pass)
print(acc1.reset_pass())