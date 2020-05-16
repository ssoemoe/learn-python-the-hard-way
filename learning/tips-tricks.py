# learn from geeks for geeks
# swapping
a , b = 1 , 2
print(a,b)

# reversing a string
string = "esrever"
print(string[::-1])

# comparison
print("-1 <= 0.1 <= 1 is", (-1 <= 0.1 <= 1))

# print the file paths of imported modules
import os, socket
print(os, ",", socket)

# use of enums
class Test:
    a, b, c = range(3)

print(Test.a, Test.b, Test.c)

# joining the array
names = ["Shane", "Khant", "Soe", "Moe"]
print(" ".join(names))

# returning multiple values from functions as a tuple
def get_weekend():
    return "Sat", "Sun"
(x,y) = get_weekend()
print(x,y,"is",type(get_weekend()))

# getting the most frequent value
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 2]
print(set(test))
print(max(set(test), key=test.count))

# checking memory usage of a variable in bytes
import sys
x = 1000000
print(sys.getsizeof(x), "bytes")

# print string n times
n = 10
print("test " * n)

# checking anagram
from collections import Counter
print(Counter("test") == Counter("tset"))

# using ternary operator
class A:
    def p(self):
        print("A")

class B:
    def p(self):
        print("B")

ternary = 100 if 10 == 10 else 90

# ternary operator can be used for objects too
a = A()
b = B()
(a if ternary == 90 else b).p()

# multiline print
multiline_str = """I am Shane.
Nice to meet you!
"""
print(multiline_str)

a,b,c = [1,2,3]
print(a,b,c)



