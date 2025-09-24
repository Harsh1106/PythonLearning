age = int(input("Enter your age: "))
if age >= 18 and age < 35:
    print("You are an adult.")
elif 13 <= age and age< 18:
    print("You are a teenager.")
elif age >= 35:
    print("You are middle-aged.")
else:
    print("You are a child.")

#nested if-else
age = 70
flag = True
if age >= 60:
    if flag:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("Not eligible for senior citizen benefits.")
    

#ternary operator
age = 20
s = "Adult" if age >= 18 else "Minor"
print(s)

c = "Eligible" if 4>3 else "Not Eligible"
print(c)


#match-case (Python 3.10+)
number = 2
match number:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case _:
        print("Other number")