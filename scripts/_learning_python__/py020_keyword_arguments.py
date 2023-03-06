# Keyword arguments = assigning an identifier for the arguments being passed to the function.
# The sequent of the arguments does not matter. The function will recognize the arguments by its identifier, and will use the arguments.

# The function will have limited number of arguments.
def greet(first_name, last_name, day):
    print("Namaster, " + first_name + " " + last_name + ". " + "It's " + day + " today.")
    print("Have a nice day.")

# greet("Ashish", "Kumar", "Sunday")
# greet("Kumar", "Ashish", "Sunday")
# greet(first_name="Ashish", last_name="Kumar", day="Sunday")
greet(first_name="Kumar", last_name="Ashish", day="Sunday")

# **kwargs stores all the arguments into a dictionary.
# We can pass varying amount of arguments to the function.
def ramayan(**kwargs):
    # print("Ramayan: " + kwargs["first"] + ", " + kwargs["second"])
    print("Ramayan: ", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

ramayan(first="Ram", second="Lakshman", third="Bharat", fourth="shatrughna", fifth="Sita", sixth="Ravan", seventh="Hanuman", eighth="Lav", nineth="Kush" )

