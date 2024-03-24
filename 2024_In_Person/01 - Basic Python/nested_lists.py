# This is a list full of lists
list_of_lists = [[0, 1, 2], [3, 4, 5]]

# Loop through the main list
for my_list in list_of_lists:
    print(my_list)
    # Loop through the sub-lists
    for number in my_list:
        print(number)