# Import some code someone else made
from random import choice

# String
string = "Jeremy Kevin Eunice Jennifer Kim Joey"
# Make the string a list
my_list = string.split()
# The best student is the first
best_student = my_list[0:2]

# Dictionary of students’ favorite colors
favorite_colors = {
    # key    : # value
    "Kevin"  : "Orange", 
    "Eunice" : "Blue", 
    "Mel"    : "Green"
    }
# Set Mel’s favorite color to be a number and then a list
favorite_colors["Mel"] = 2
favorite_colors["Mel"] = my_list

# Print the dictionary
print(favorite_colors)
