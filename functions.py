def fun():
    print("Hello")
fun()


def fun(a):
    if a % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(fun(3))
print(fun(4))

def fun(a, b):
    return a + b
print(fun(2, 3))

def abc(a, b=10):
    print("x:",a)
    print("y:",b)
abc(2)

def name(fname, lname):
    print(fname, lname)
name("Harsh", "Raj")
print("Abc", "Def")


# *args is Non-Keyword Variable Length Arguments
# **kwargs is Keyword Variable Length Arguments
def myFun(*args, **kwargs):
    print("Non-keyword arguments (*args):")
    for i in args:
        print(i)
    
    print("\n Keyword Arguments (**kwargs):")
    for i, j in kwargs.items():
        print(f"{i} == {j}")
    
myFun('Hello', 'Welcome', name="Harsh", age=23)


def f1():
    s = "I love Python"
    def f2():
        print(s)
    f2()
f1()


def cube(x):
    return x*x*x
cube1 = lambda x: x*x*x # Anonymous Function(lambda function)
print(cube(3))
print(cube1(4))

def my(x):
    x[0] = 20
list = [10, 11, 12]
my(list)
print(list)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
print(fact(5))