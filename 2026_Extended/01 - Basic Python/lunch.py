# Gather data about lunch preferences
lunch_choices = {
    "Dorian": "Ramen",
    "Clara": "Any caffeine cold brew espresso any caffeine",
    "Katie": "Thai",
    "Rochell": "Tacos",
    "Wei Wei": "Spice",
    "Rebecca": "Sandwich",
    "Andrew": "Thai",
    "Francine": "Japanese",
    "Sergio": "Italian",
    "Jasmin": "Thai",
    "Shiqing": "Japanese",
    "Vivian": "NOODLES",
    "Fai": "Soups",
    "Eric": "Korean",
    "Dylan": "Pizza",
    "Eugene": "Katz"
}

# Put all of the votes into a list
preferences = list(lunch_choices.values())

# Make a new empty list to collect... 
uniques = []
for preference in preferences:
    # the votes and how often they appear
    my_addition = (preferences.count(preference), preference)
    # Only add to the list if it's not already present
    if my_addition not in uniques:
        uniques.append(my_addition)
        
# Sort the list
uniques = sorted(uniques)
# Reverse it (descending)
uniques.reverse()
# Print the winner!
print(uniques[0])

## The random selection way!
# print(choice(list(lunch_choices.values())))

    
