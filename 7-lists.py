# list is a sequence of values, but in list, they can be any type
# values in list are called elements/items
cheeses = ['cheddar', 'edam', 'gouda']
empty = []  # empty list
print(cheeses)      # output: ['cheddar','edam','gouda']
print(empty)        # output: []


# lists are mutable, we can change the order of items in a list or re-assign an item in a list
numbers = [17, 234]
numbers[1] = 5      # replace with new item
print(numbers)      # output: [17,5]
# numbers[2] = 19     # cannot insert new items
# print(numbers)


# traversing a list
for cheese in cheeses:
    print(cheese)


# list operations
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)    # output: [1,2,3,4,5,6]
d = a * 3
print(d)    # output: [1,2,3,1,2,3,1,2,3]


# list slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])   # output: ['b','c']
t[1:3] = ['x', 'y']
print(t)        # output: ['a','x','y','d','e','f']


# list methods
t = ['a', 'b', 'c']
print(t)    # output: ['a','b','c']
t.append('d')
print(t)    # output: ['a','b','c','d']

t1 = ['a', 'b', 'c']
t2 = ['d', 'e', 'f']
t1.extend(t2)   # t2 unmodified
print(t1)       # output: ['a','b','c','d','e','f']

t = ['d', 'c', 'e', 'b', 'a']
print(t)    # output: ['d','c','e','b','a']
t.sort()
print(t)    # output: ['a','b','c','d','e']


# deleting elements/items
t = ['a', 'b', 'c']
# pop modifies the list and returns the element that was removed.
x = t.pop(1)
# if we don't provide an index, it deletes and returns the last element.
print(t)    # output: ['a','c']
print(x)    # output: b

t = ['a', 'b', 'c']
# if we don't need the removed value, use `del`
del t[1]
print(t)    # output: ['a','c']

t = ['a', 'b', 'c']
# if we know the items we want to remove but not the index, use `remove`
t.remove('b')
print(t)    # output: ['a','c']

t = ['a', 'b', 'c', 'd', 'e', 'f']
# remove more than one items, use `del` with a slice
del t[1:5]
print(t)    # output: ['a','f']


# lists and functions
nums = [3, 41, 21, 9, 73, 15]
print(len(nums))                # output: 6
print(max(nums))                # output: 73
print(min(nums))                # output: 3
print(sum(nums))                # output: 162
print(sum(nums) / len(nums))    # output: 27.0
# rewrite the average calculation
total = 0
count = 0
while (True):
    inp = input('enter a number:')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('average:', average)
# simpler alternative
numlist = list()
while (True):
    inp = input('enter a number:')
    if inp == 'done':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('average:', average)


# lists and strings
s = 'spam'
t = list(s)     # `list` built-in function
print(t)        # output: ['s','p','a','m']
s = 'pinning for the fjords'
t = s.split()   # `split` method to break string into words
print(t)        # output: ['pinning','for','the','fjords']
s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)  # output: ['spam','spam','spam']
t = ['pinning', 'for', 'the', 'fjords']
delimiter = ' '
# `join` takes a list of strings and concatenates the elements.
delimiter.join(t)   # output: 'pinning for the fjords


# parsing lines
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(words[2])


# objects and values
a = 'banana'
b = 'banana'
# we know that `a` and `b` both refer to a string, but we don't know whether they refer to the same string
# 1-`a` and `b` refer to 2 different objects that have the same value
# 2-they refer to the same object
# to check
print(a is b)   # output: True
# when two lists are created, we get two objects
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)   # output: False
# two lists are equilavent, because they have the same elements,
# but not identical, because they are not the same object


# aliasing
a = [1, 2, 3]
b = a
# both variables refer to the same object
print(a is b)   # output: True
b[0] = 19
# if aliased object is mutable, changes made with one alias effect the other
print(a)        # output: [19,2,3]


# list arguments
def delete_head(t):
    del t[0]


letters = ['a', 'b', 'c']
# when we pass list to function, the function gets a reference to the list
# when function modifies a list parameter, the caller sees the change
delete_head(letters)
print(letters)  # output: ['b','c']

# it is important to distinguish between operations that modify lists and operations that create new lists
t1 = [1, 2]
t2 = t1.append(3)
print(t1)   # output: [1,2,3]
print(t2)   # output: None

t3 = t1
print(t3)           # output: [1,2,3]
print(t2 is t3)     # output: False


def bad_del_head(t):
    # this difference is importance when we write functions that are supposed to modify lists
    # this function does not delete the head of a list
    t = t[1:]
    # the slice operator creates a new list and the assignment makes `t` refer to it
    # but none of that has any effect on the list that was passed as an argument


t = ['a', 'b', 'c']
print(bad_del_head(t))  # output: None
print(t)                # output: ['a','b','c']


def tail(t):
    # alternative - write function that creates and returns a new list
    # this function leaves the original list unmodified
    return t[1:]


letters = ['a', 'b', 'c']
print(tail(letters))    # output: ['b','c']
print(letters)          # output: ['a','b','c']
