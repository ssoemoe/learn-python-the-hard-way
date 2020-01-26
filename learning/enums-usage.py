import enum

class Shapes(enum.Enum):
    SPADE = 0
    HEART = 1
    DIAMOND = 2
    CLUB = 3

class Num(enum.Enum):
    TEST = 0
    TEST1= 1

# printing names
print(Shapes.CLUB.name)

# printing just original values\
print(Shapes.SPADE)

# will return false
print(Shapes.HEART == Num.TEST1)

# Used as dict keys
dict = {}
dict[Shapes.HEART] = "Original"
dict[Num.TEST1] = "Changed"
print(dict)