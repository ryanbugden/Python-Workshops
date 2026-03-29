from random import choice

# Make a function that chooses a random coordinate from a list of coordinates.
def choose_random_coordinate(list_of_coords):
    return choice(list_of_coords)

# Establish 2 data-sets
coord_list_1 = [(100, 200), (300, 400), (500, 600)]
coord_list_2 = [(50, 150), (250, 350)]

winning_coord_1 = choose_random_coordinate(coord_list_1)
winning_coord_2 = choose_random_coordinate(coord_list_2)

# See the results.
print(winning_coord_1)
print(winning_coord_2)
print()
# Stored variable hasn't changed. Ran function once.
print(winning_coord_1)
print(winning_coord_1)
# This might be different, because it runs the function anew
print(choose_random_coordinate(coord_list_1))

