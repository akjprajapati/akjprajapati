# Nested loos = A loop inside loop.
# The inner loop will finish all its iteration before moving ahead for the next iteration of the outer loop.

rows = int(input("Please specify number of rows: "))
columns = int(input("Please specify number of columns: "))
symbol = input("Please specify a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end='')
    print()