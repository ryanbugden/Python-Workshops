from random import choice

def choose_random_coordinate(list_of_coords):
    my_coord = choice(list_of_coords)
    return my_coord

coord_list_1 = [(100, 200), (300, 400), (500, 600)]
coord_list_2 = [(50, 150), (250, 350)]

winning_coord_1 = choose_random_coordinate(coord_list_1)
winning_coord_2 = choose_random_coordinate(coord_list_2)

print(winning_coord_1)
print(winning_coord_2)
print()
print(winning_coord_1)
print(winning_coord_1)
print(choose_random_coordinate(coord_list_1))

