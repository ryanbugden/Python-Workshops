my_dict = {
    "Ryan": 5,
    "Green": 4,
    }
# dictionary.items() makes a dictionary into a list of tuples
for whatever, value in my_dict.items():
    print(whatever, value)
    
print()
list_of_tuples = [("DrawBot", 2), (3, "Python")]
for turtle, random_word_or_something in list_of_tuples:
    print(turtle, random_word_or_something)

print()
list_of_coordinates = [(0, 200), (300, 400)]
for (x, y) in list_of_coordinates:
    print(y) 