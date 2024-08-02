# Creating a list, a dictionary, and a set
my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {1, 2, 3}

# Basic operations on the list
# Adding an element
my_list.append(4)
print("List after adding an element:", my_list)

# Removing an element
my_list.remove(2)
print("List after removing an element:", my_list)

# Modifying an element
my_list[1] = 5
print("List after modifying an element:", my_list)

# Basic operations on the dictionary
# Adding a key-value pair
my_dict['d'] = 4
print("Dictionary after adding a key-value pair:", my_dict)

# Removing a key-value pair
del my_dict['b']
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value
my_dict['a'] = 10
print("Dictionary after modifying a value:", my_dict)

# Basic operations on the set
# Adding an element
my_set.add(4)
print("Set after adding an element:", my_set)

# Removing an element
my_set.remove(2)
print("Set after removing an element:", my_set)

# Modifying elements in a set is not directly possible since sets are unordered collections,
# but we can remove and add elements to achieve the modification
my_set.discard(1)
my_set.add(5)
print("Set after modifying elements (removing 1 and adding 5):", my_set)
