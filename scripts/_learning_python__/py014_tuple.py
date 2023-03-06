# tuple = a collection of items which is ordered and unchageable.
#           it is used to group related data.

family = ("father", "mother",  "wife", "sister", "sister", "brother", "sister in law", "son", "son", "daughter")

print(family.count("sister"))          # prints the number of occurrences of the itme in the tuple.
print(family.index("wife"))            # prints the index of the item.

for i in family:
    print(i)

if "daughter" in family:
    print("I've a daughter!")