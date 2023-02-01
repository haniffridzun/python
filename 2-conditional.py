# boolean expressions
print(5 == 5)   # output: True
print(1 == 9)   # output: False


# logical operators - and, or, not
print(1 > 0 and 5 < 3)  # output: False
print(1 > 0 or 5 < 3)   # output: True


# contitional execution
x = int(input('insert an integer: '))
if x > 0:
    print('x is positive')


# alternative execution
x = int(input('insert an integer: '))
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')


# chained conditionals
x = int(input('insert first integer: '))
y = int(input('insert second integer: '))
if x < y:
    print('first is less than second')
elif x > y:
    print('first is greater than y')
else:
    print('first and second are equal')


# catching exceptions using try and except
inp = input('enter Fahrenheit temperature: ')
try:
    fahr = float(inp)
    celc = (fahr - 32.0) * 5.0 / 9.0
    print('in celcius is', celc)
except:
    print('please enter a number')
