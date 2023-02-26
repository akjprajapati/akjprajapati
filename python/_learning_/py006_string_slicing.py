# Slicing =  Create a sub string by extracting elements from another string.
#            indexing[] or slice()
#            [start:stop:step]

name = "Ashish Kumar"

# Use of indexing method for slicing a string.
# first_name = name[0:6]    # Start index and stop index specified.
# first_name = name[:6]     # Start index is taken as '0' by default if not specified.
first_name = name[:-6]      # This is reverse indexing. It counts from the end and represented by a negative number.

# last_name = name[7:12]    # Start index and stop index specified.
# last_name = name[7:]      # Stop index is taken as the last index by default if not specified.
last_name = name[-5:]       # This is reverse indexing. It counts from the end and represented by a negative number.

print(first_name + " " + last_name)

# reversed_name = name[-1:0:-1]     # Reverse indexing to print the whole string in reverse with step 1.
reversed_name = name[::-1]          # Reverse indexing to print the whole string in reverse with step 1.
print(reversed_name)

# Use of slice function for slicing a stirng.
website1 = "https://www.domain.tld"
website2 = "https://www.sub.domain.tld"

domain_name = slice(12,-4)

print(website1[domain_name])
print(website2[domain_name])
