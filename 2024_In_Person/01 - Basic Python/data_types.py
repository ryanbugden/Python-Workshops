# Numbers
my_number = 2
print(my_number)

# Lists
my_list = ["hello", 1, 3]
print(my_list[0])
my_list[0] = "other random thing"
print(my_list)

# Tuples
my_tuple = ("hello", 1, 3)
# Can't change tuples :(
print(my_tuple)
my_listified_tuple = list(my_tuple)
my_listified_tuple[0] = "other random thing"
my_tuple = tuple(my_listified_tuple)
print(my_tuple)

# Dictionaries
my_dictionary = {"key 1": 2, "other key": 10}
other_dictionary = {"random key": "New York"}
print(my_dictionary)
print(my_dictionary["key 1"])
print(my_dictionary["other key"])
my_dictionary["key 1"] = "apple"
print(my_dictionary)
my_dictionary.update(other_dictionary)
(my_dictionary)



