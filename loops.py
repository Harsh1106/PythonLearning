n = 5
for i in range(0, n):
    print(i)

li = [1, 2, 3, 4, 5]
for i in li:
    print(i)

tup = ("harsh", "raj", "abc")
for i in tup:
    print(i)

s = "Harsh"
for i in s:
    print(i)

d = dict({"harsh": "person", "raj": "person", "abc": "company"})
for i  in d:
    print("%s %s" % (i, d[i]))

li = ["harsh", "raj", "abc"]
for index in range(len(li)):
    print(li[index])

for index in range(len(li)):
    print(li[index])
else:
    print("Inside else block")

# while loop
count = 0
while count < 5:
    count+=1
    print("Hi")
flag = 0
while flag < 3:
    print("Yo")
    flag+=1
else:
    print("Bye")

for i in 'harsh':
    if i == 'h' or i == 's':
        continue
    print(i)

for i in 'harsh':
    if i == 'h' or i == 's':
        break
    print(i)

for i in 'harsh':
    pass
print(i)

