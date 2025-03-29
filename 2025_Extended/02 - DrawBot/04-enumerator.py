my_list = ["one", "two", "three"]

# Use enumerate to get the index of the list as you loop through it
for i, item in enumerate(my_list):
    # Check to see if there is leftover when you divide the index by 2
    if i % 2:
        print(item)