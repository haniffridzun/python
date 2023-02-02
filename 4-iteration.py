# while statement
n = 3
while n > 0:
    print(n)
    n = n - 1

print('blastoff!')
# output:
# 5
# 4
# 3
# 2
# 1
# blastoff!


n = 5
while True:
    line = input('>')
    if line == 'done':
        break       # break once user type 'done'
    print(line)

print('done')


while True:
    line = input('>')
    if line[0] == '#':
        continue    # all lines with # sign will not be printed / skipped
    if line == 'done':
        break       # break once user type 'done
    print(line)

print('done!')


# definite loops using for
friends = ['joseph', 'glenn', 'sally']
for friend in friends:
    print('happy new year,', friend)

print('done!')


# counting and summming loops
count = 0
for iterVar in [3, 41, 12, 9, 74, 15]:
    count = count + 1

print('count:', count)
# output: 6


# max and min loops
largest = None
print('before: ', largest)
for iterVar in [3, 41, 12, 9, 74, 15]:
    if largest is None or iterVar > largest:
        largest = iterVar

    print('loop:', iterVar, largest)

print('largest:', largest)
