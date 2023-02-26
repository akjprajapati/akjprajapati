# if = checks truthiness of a condition to execute a block of code.
#
age = float(input("What is your age? : "))

if 60 < age <= 100:
    print("Hello, You are a senior citizen!")
elif 18 < age <= 60:
    print("You are an adult person!")
elif 12 < age <= 18:
    print("You are a Teenager!")
elif 3 < age <=12:
    print("You are a child!")
elif 1 < age <= 3:
    print("You are a toddler!")
elif 0 < age <= 1:
    print("You are an infant")
else:
    print("You are " + str(age) + " years old!")