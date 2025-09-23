# None, Numeric, List, Tuple, Set, Range, Dictionary 
# Numeric: int, float, complex, bool
num = 2.5
print(type(num)) # float
num = 5
print(type(num)) # int
num = 3 + 5j # j represents the imaginary part
print(type(num)) # complex

a = 5.6
b = int(a) # convert float to int known as type casting
print(type(b)) # int

k = float(b) # convert int to float
print(type(k)) # float

k = 6
c = complex(b, k) # convert int to complex
print(type(c)) # complex
print(c) # (5+6j)

bool = b < k
print(type(bool)) # bool
print(bool) # True


# the below data types falls under the category of sequence and collection data types

lst = [1, 2.5, 'hello', True] # list is mutable
print(type(lst)) # list

set = {1, 2.5, 'hello', True} # set is mutable and unordered
print(type(set)) # set

tup = (1, 2.5, 'hello', True) # tuple is immutable
print(type(tup)) # tuple

str = "Harsh"
print(type(str)) # str

str = 'a'
print(type(str)) # str

range(10) # immutable sequence of numbers
print(type(range(10))) # range

list(range(10)) # convert range to list
print(list(range(10))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 10, 2))) # [2, 4, 6, 8] print even numbers from 2 to 10


dict = {'harsh':'motorola', 'rahul':'samsung', 'aman':'realme'} # dictionary is mutable and unordered
print(type(dict)) # dict
print(dict) # {'harsh': 'motorola', 'rahul': 'samsung', 'aman': 'realme'}
print(dict.keys())
print(dict.values())
print(dict['rahul'])

print(dict.get('aman')) # realme
dict['aman'] = 'oneplus' # update value of key 'aman'
print(dict) # {'harsh': 'motorola', 'rahul': 'samsung', 'aman': 'oneplus'}
