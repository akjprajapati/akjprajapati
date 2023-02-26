# index operator [] = to access and element of str, list, tuple etc.

word = "technology"
term = "information technology"

if (word[0].islower()):
    word = word.capitalize()
print(word)

first_word = term[:11].capitalize()
last_word = term[12:].capitalize()
first_character_w1 = term[0].upper()
first_character_w2 = term[12].upper()

print("Full form of " + first_character_w1 + "." + first_character_w2 + "." +" is: " + first_word + " " + last_word)
