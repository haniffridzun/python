# function is a named sequence of statements that performs a computation


# built-in function int convert float/string into integer
import random
import math     # this statement creates a module object named math
x = print(type(int('123')))
# built-in function float convert integer/string into floating-point numbers
y = print(type(float(123)))
# built-in function str convert integer/float into string
z = print(type(str(123.1)))


# Python has math module that provides most of mathematical functions
# the module object contains the functions and variables defined in the module.
# to access one of the functions, we have to specify the name of the module and name of the function
radians = 0.7
height = math.sin(radians)


# random module provides functions that generate pseudo-random numbers
for i in range(10):
    j = random.random()
    print(j)

# randit takes parameters low and high, and returns an integer between low and high
rand = random.randint(1, 9)
print(rand)


# adding new functions using def
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


# once we have defined a functions, we can use it inside another function.
def repeat_lyrics():
    print_lyrics()
    print_lyrics()


# call each functions after the function definition, never before
print_lyrics()
repeat_lyrics()


# parameters and arguments
def addTwo(a, b):       # it required 2 arguments, these arguments assigned to parameter a and b
    added = a + b
    return added


a = addTwo(10, 9)
print(a)
