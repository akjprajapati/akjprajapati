# **kwargs stores all the arguments into a dictionary.

def ramayan(**kwargs):
    # print("Ramayan: " + kwargs["first"] + ", " + kwargs["second"])
    print("Ramayan: ", end=" ")
    for key,value in kwargs.items():
        print(value, end=" ")

ramayan(first="Ram", second="Lakshman", third="Bharat", fourth="shatrughna", fifth="Sita", sixth="Ravan", seventh="Hanuman", eighth="Lav", nineth="Kush" )


