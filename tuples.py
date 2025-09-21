# it is immutable where list is mutable
# iteration is faster in tuple than list
tup = (1, 2, 3, 4, 5)
print(tup)
print(type(tup))
print(tup[1])
print(tup.count(3)) # counts the number of occurrences of an element
print(tup.index(4)) # returns the index of the first occurrence of an element