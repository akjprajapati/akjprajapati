# while loop = a statement that will execute the block of code as long as its condition is true.

fist_name = ""

while len(fist_name) == 0:
    fist_name = input("Please enter your first name: ")

print("Hi, " + fist_name)


last_name = None

while not last_name:
    last_name = input("Please enter your last name: ")

print("Hello, Mr. " + last_name)
