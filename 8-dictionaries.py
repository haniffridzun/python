# dictionary is like a list, but more general. in list, index positions have to be integers;
# in dictionary, the indices can be almost any type type
# each key maps to a value, key-value pair
import string
eng2sp = dict()
print(eng2sp)   # output: {}
# function dict creates a new dictionary
# to add item to the dictionary, we can use square brackets
eng2sp['one'] = 'uno'
print(eng2sp)   # output: {'one':'uno'}
# add 3 items
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)   # output: {'one':'uno', 'two':'dos', 'three':'tres'}
# look up for the value using key
print(eng2sp['two'])    # output: 'dos'
# if the key isn't in the dictionary
# print(eng2sp['four'])   # output: KeyError: 'four'
# check the key in dictionary
'one' in eng2sp     # output: True
'uno' in eng2sp     # output: False


# dictionary as a set of counters
word = 'brontosaurus'
d = dict()
for c in word:
    if c not in d:
        d[c] = 1
    else:
        d[c] = d[c] + 1
print(d)
# output: {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
# create a dictionary with characters as keys and counters as the corresponding values.
# the first time we see a character, we could add an item to the dictionary.
# after that we would increment the value of an existing item.

# get method - takes a key and a default value.
counts = {'chuck': 1, 'annie': 42, 'jan': 100}
print(counts.get('jan', 0))     # output: 100
# if the key appears in the dicitoanry, it returns the corresponding value,
# otherwise it returns the default value = 0

# rewrite the histogram loop more concisely
word = 'brontosaurus'
d = dict()
for c in word:
    d[c] = d.get(c, 0) + 1
print(d)
# output: {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}


# dictionaries and files
fname = input('enter the file name:')
try:
    fhand = open(fname)
except:
    print('file cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] + 1
print(counts)


# looping and dictionaries
# use dictionary as sequence in a for loop, it traverses the keys of the dictionaries
counts = {'chuck': 1, 'annie': 43, 'jan': 100}
for key in counts:
    print(key, counts[key])
# output:
# jan 100
# chuck 1
# annie 43
# the key are in no particular order.

# if we want to print keys in alphabetical order, we first make a list of the keys
counts = {'chuck': 1, 'annie': 31, 'han': 100}
key_list = list(counts.key())
print(key_list)
# output: ['han', 'chuck', 'annie']
key_list.sort()
# output: ['annie','chuck', 'han']
for key in key_list:
    print(key, counts[key])
# output:
# annie 31
# chuck 1
# han 100


# text parsing

fname = input('enter the file name:')
try:
    fhand = open(fname)
except:
    print('file cannot be opened:', fname)
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    line = line.translate(line.maketrans(',', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = 1
    else:
        counts[word] += 1
print(counts)
