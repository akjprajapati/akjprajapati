# loop control statement = it changes the behaviour of iteration depending on the contitions.
#
# break = it terminates the loops entirely.
# continue = skips an interation and moves to the next iterations.
# pass = its used as a placeholder to skip only one specific value in the range of loop.

# use of 'break'.
while True:
    name = input("Enter your name: ")
    if name != "":
        print("Hello " + name + ".")
        break

#  use of 'continue'.
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end='')

# use of 'pass'.
for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)

