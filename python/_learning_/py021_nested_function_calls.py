# nested function = a function is called inside another function.
#                   inner most function call is executed first and its return / output is used as arguments for the outer function.

# # Example 1
# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print("Number: " + str(num))

# Example 2
print(round(abs(float(input("Enter a whole positive number: ")))))

