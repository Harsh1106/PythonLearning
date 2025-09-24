import sys
x = int(input("Enter first number: "))
# print(type(x)) # By default, input() returns a string
y = int(input("Enter second number: "))
z = x + y
print(z)

ch = input("Enter a character: ")[0] # To get a single character
print(ch)

result = eval(input('enter an expression'))
print(result)

a = int(sys.argv[1])
b = int(sys.argv[2])
z = a + b
print(z)