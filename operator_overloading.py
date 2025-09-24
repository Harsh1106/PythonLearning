class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real, "i +", self.img, "j")

    def __add__(self, obj): #dunder method for operator overloading
        real = self.real + obj.real
        img = self.img + obj.img
        return Complex(real, img)
    
    def __sub__(self, obj):
        real = self.real - obj.real
        img = self.img - obj.img
        return Complex(real, img)

num1 = Complex(2, 3)
num1.showNumber()

num2 = Complex(5, 6)
num2.showNumber()

# num3 = num1.add(num2)
# print(num3.showNumber())

num3 = num1 + num2 #internally calls __add__ method
num3.showNumber()

num4 = num1 - num2 #internally calls __sub__ method
num4.showNumber()