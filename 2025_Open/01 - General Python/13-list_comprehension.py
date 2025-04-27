# Set up
suffix = ".case"
my_list = ["a", "b", "c"]

# Starting with an empty list and filling it as you go
new_list = []
for item in my_list:
    new_list.append(item + suffix)   
print(new_list)

# List comprehension
other_list = [item + suffix for item in my_list]
print(other_list)