# string is a sequence of characters
fruit = 'banana'
letter = fruit[1]
print(letter)   # output: a


# getting the length of string using len()
fruit = 'strawberry'
str_length = len(fruit)
print(str_length)   # output: 10


# get the last character from string
char_last = fruit[str_length - 1]   # because index start at 0, so last index is len() - 1
print(char_last)    # output: y


# traversal though a string using loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1   # print each characters in fruit

for char in fruit:
    print(char)     # similar output with while loop above


# string slices - a segment of a string is called a slice
s = 'monty python'
print(s[0:5])   # output: monty
print(s[6:12])  # output: python
# same output
print(s[:5])    # output: monty
print(s[6:])    # output: python


# strings are immutable
greeting = 'hello, world'
# greeting[0] = 'j'   # output: TypeError: 'str' object does not support item assignment
# assign new string based on the original string
new_greeting = 'j' + greeting[1:]
print(new_greeting)
# it has no effect on the original string


# looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':   # count the number of occurence of letter a
        count = count + 1

print(count)    # output: 3


# in operater
print('a' in 'banana')
print('seed' in 'banana')


# string comparison
word = input('what is your favourite fruit: ')
if word < 'banana':
    print('your word, ' + word + ', comes before banana')
elif word > 'banana':
    print('your word, ' + word + ', comes after banana')
else:
    print('all right, bananas')
# all the uppercase letters come before all the lowercase letters
# a common way to address this problem is to convert strings to standard format


# string methods
stuff = 'hello world'
print(type(stuff))              # output: <class 'str'>
print(dir(stuff))               # output: list all methods available for the object
print(help(str.capitalize))     # output: get documentation of the method
# example of string method
print(stuff.upper())            # output:   HELLO WORLD
print(stuff.find('r'))          # output: 8
# remove white space (spaces, tabs, newlines)
line = '    here we go  again           '
print(line)                     # output:     here we go  again           
print(line.strip())             # output: here we go again


# parsing strings
data = 'from stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atPos = data.find('@')
print(atPos)    # output: 21
afPos = data.find(' ', atPos)
print(afPos)    # output: 31
host = data[atPos: afPos + 1]
print(host)     # output: uct.ac.za


# % format operator - allows us to construct strins, replacing parts of the strings
# when applied to integers, % is the modulus operator
# when applied to string, % is the format operator
camels = 42
str_camels = 'I have spotted %d camels' % camels
print(str_camels)   # output: 'I have spotted 42 camels'
# %d to format an integer
# %g to format a floating-point number
# %s to format a string
spot_camels = 'in %d years, I have spotted %g %s' % (3, 0.1, 'camels')
print(spot_camels)