# Looping through lists
my_list = ["hello", 1, 3]
for item in my_list:
    print(item)

# Looping through tuples
my_tuple = ("hello", 1, 3)
for item in my_tuple:
    print(item)

# Looping through dictionaries
my_dictionary = {"key1": [3, 4, "b"], "otherkey": [10, 2, "a"]}
print(my_dictionary.items())
for key, a_list in my_dictionary.items():
    print(a_list)
    for pizza in a_list:
        print(pizza)

# Looping through letters in a string
my_string = "random text"
for letter in my_string:
    print(letter)