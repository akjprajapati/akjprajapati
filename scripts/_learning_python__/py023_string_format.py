# str.format() = A method which gives control to a user in formating and displeying a string.

fox_adj = "quick"
color = "brown"
animal_1 = "fox"
dog_adj = "Lazy"
animal_2 = "dog"

print("A " + fox_adj + " " + color + " " + animal_1 + " jumps over the " + dog_adj + " " + animal_2 + ".")

print("A {} {} {} jumps over the {} {}.".format("quick", "brown", "fox", "lazy", "dog"))

print("A {} {} {} jumps over the {} {}.".format(fox_adj, color,animal_1, dog_adj, animal_2))
