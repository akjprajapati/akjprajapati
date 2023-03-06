# set  = a collection which is unordered, un-indexed, and it contains no duplicates.

fruits = {"avocado", "tomato", "carrot", "apple", "orange", "mango", "avocado"}
vegetables = {"tomato", "carrot", "potato", "redis", "onion", "ginger", "carrot"}

fruits.add("banana")
fruits.remove("avocado")

# for i in fruits:
#     if i != "":
#         print(i)
#     else:
#         print("The set is empty now.")

# fruits.clear()                          # It clears the set entirely. All items gone.

# fruits.update(vegetables)
# for i in fruits:
#     print(i)

# fruits_n_veg = fruits.union(vegetables)
# for i in fruits_n_veg:
#     print(i)

print(fruits.difference(vegetables))            # Prints the items of fruits which are not in vegetables.
print(vegetables.difference(fruits))            # Prints the items of vegetables which are not in fruits.
print(fruits.intersection(vegetables))          # Prints the common items in both the sets.
print(vegetables.intersection(fruits))          # Prints the common items in both the sets.

