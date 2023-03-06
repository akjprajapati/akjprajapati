# for loop = a statement that will execute the block of code for a limited amount of times.
#
# for loop = limited iteration against a range.
# while loop = unlimited iterations against a condition.

import time

# below loop will print 0 to 9 as it follows the index provided the range and excludes the last value of the range.
for i in range(10):
    print(i, end=' ')
print("...")

# To print the numbers 10 to 20 we will be adding '1' in the output.
for i in range(20, 30):
    print(i+1, end=' ')
print("...")

# To print the last value of the range including the fist value, we'll add '1' in the last limit of the range.
for i in range(40, 50+1):
    print(i, end=' ')
print("...")

# Iteration with a step of '2'. It'll print every 2nd number in the range.
for i in range(60, 100+1, 2):
    print(i, end=' ')
print("...")

# Iteration on a string.
for i in "Ashish Kumar":
    print(i, end=' ')
print("...")

# Count down of 10 seconds using time module.
for i in range(10, 0, -1):
    print(i, end=' ')
    time.sleep(1)
print("Count down complete!")
