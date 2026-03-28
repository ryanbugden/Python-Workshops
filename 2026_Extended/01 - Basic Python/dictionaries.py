# Make a dictionary where the keys are student names and the values are favorite colors.
favorite_colors = {
    "Sergio": "Red", 
    "Jasmin": "Green", 
    "Shiqing": ["Blue", "White"]
}

## A commented-out piece of code
# print(favorite_colors)
# print(favorite_colors.keys())
# print(favorite_colors.values())
# print(favorite_colors.items())

# Get Shiqing’s favorite color(s)
print(favorite_colors["Shiqing"])
# Add Purple to Shiqing’s favorite colors
favorite_colors["Shiqing"].append("Purple")
# Check all of her favorite colors again
print(favorite_colors["Shiqing"])


