# scope = local scope. In this case a variable is defined inside the function or a block of code to be used in that region only.
#         global scope. In this case a variable is defined out side of any block of code and it is available to be used globaly.
#         Whena a varialbe is called python first looks for a local variabla and ifts not found then it looks for a global variable.

name = "python2.7"      # This is a global variable that is defined to be used anywhere.

def display_name():
    name = "python3.9" # This is a local variable that is defined to be used only in this function.
    print(name)

display_name()
print(name)

# Python follows LEGB rule for variables.
# L = local.
# E = Enclosing.
# G = Global.
# B = Built-in.
