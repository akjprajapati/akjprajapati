# Logical operators = and, or, not = to check truthiness of two or more conditions in single if statement.
# and = this logic is used to check that all the condition must satisfy to execute the block of code.
# or = this logic is used to check that any one condition must satisfy to execute the code.
# not = it is used to flip the condition(s).

# Variable declaration.
temperature = float(input("What is the temperature here? : "))

# If statements.

# if temperature >= 0 and temperature <= 30:    # Using the and logic.
if 15 <= temperature <= 35:
    print("The temperature is good today.")
elif temperature <= 20 or temperature >= 35:
    print("Temperature is not favourable to go outside.")
