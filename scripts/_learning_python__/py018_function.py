# Function = a reusable block of code which is executed only when it is called.

def greet(first_name, last_name, age):
    print("Namaste, " + first_name + " " + last_name + ".")
    print("You are " + str(age) + " years old. Have a nice day")


greet("Ashish", "Kumar", 34)

# A funtion with multipe arguments.
# using '*args' we can pass multiple arguments as well as varying number of arguments.

# *args = a statement with stores all the arguments in a tuple.

def add(*nums):
    sum = 0 
    nums = list(nums)
    nums[0] = 0
    for i in nums:
        sum += i
    return sum

print("The sum is: "+ str(add(1,2,3,4,5,6,7,8,9)))
