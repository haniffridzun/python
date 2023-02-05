# opening files
# when we open a file, we are asking the operating system to find 
# the file by name and make sure the file exists
fhand = open('mbox.txt')
print(fhand)    # output: <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252>


# reading files
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1

print('line count:', count)     # output: line count: 5

# read() - if we know the file is small compared to size of main memory
# we can read the whole file into one string using read method on the file handle
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp))     # output: 907


# searching through a file
fhand = open('mbox-short.txt')
for line in fhand:
    # select only those lines with the desired prefix
    if line.startswith('From: '):
        print(line)


fhand = open('mbox-short.txt')
for line in fhand:
    # use rstrip to strip whitespaces from the right side of a string
    line = line.rstrip()
    if line.startswith('From: '):
        print(line)


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    # skip uninteresting lines
    if not line.startswith('From: '):
        continue
    # process our interesting line
    print(line)


fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1: continue
    print(line)


# letting the use choose the file name
fname = input('enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('subject:'):
        count = count + 1

print('there were', count, ' subject line in', fname)


# using try, except
fname = input('enter the file name: ')
try:
    fhand = open(fname)
except:
    print('file cannot be opened:', fname)
    exit()

count = 0
for line in fhand:
    if line.startswith('subject:'):
        count = count + 1

print('there were', count, ' subject lines in', fname)


# writing files
fout = open('output.txt', 'w')
line1 = "this here's the wattle\n"
# write method of file handle object puts the data into the file
fout.write(line1)
# when done writing, we have to close the file to make sure that data is written to the disk
fout.close()