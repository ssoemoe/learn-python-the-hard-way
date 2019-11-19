# reading
file = open("demo.txt")
print(file.read())
file = open("demo.txt")
print(file.readlines())
file = open("demo.txt", "r")
print(file.readline())

print("-" * 25, " With Open ", "-" * 25)

with open("demo.txt") as file:
    print(file.read())
    file.seek(0) #rewind the memory
    print(file.readlines())
    file.seek(0)

print("-" * 25, " Importing ", "-" * 25)
from learning.contents import greeting
print(greeting)