# list = a variable which can store multiple values.

fruits = ["Apple", "mango", "orange", "banana", "avocado"]

fruits[0] = "guava"             # replace the fist item with a new item specified.

fruits.append("grapes")         # adding a new item at the end of the list.

fruits.insert(2, "coconut")     # inserting the item and a specified index place.

print(fruits)

fruits.sort()                   # Sort the items in alphabetical order.

print("Sorted list of fruits is: " + str(fruits))

fruits.remove("orange")         # Removes an item specified from the list.

print("Removed orange from the list: " + str(fruits))

fruits.pop()                    # Removes the last item in the list.

print("Removing the last item (grapes) from the list: " + str(fruits))

fruits.clear()                  # Clears the list, now the list is empty.

print("Looks like the list is empty now: " + str(fruits))


# 2D lists = a list of lists.
vegetables = ["tomato", "potato", "ladyfinger", "cauliflower", "Broccoli", "cabbage"]
dishes = ["kadhai_paner", "mashroom_masala", "shahi_paneer", "aloo_jeera"]

food = [fruits, vegetables, dishes]

print(food[2])          # print list of index 2 from food.
print(food[1][3])       # print 3rd item of 1st list.
