from learning.imports import *

def get_vals():
    return "Shane Moe", 21

first, second = get_vals()
print(f"{first} is {second} years old.")
print(split_str(first, 'h'))
print(sort_words(first))
print(reverse_str(first))