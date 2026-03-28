favorite_colors = {
    "Sergio": "Red", 
    "Jasmin": "Green", 
    "Shiqing": ["Blue", "White"]
}

# Loop through each name and favorite color in the dictionary
for name, fave in favorite_colors.items():
    # Check each item and if the favorite color is Green...
    if fave == "Green":
        # Print this!
        print(name, "has favorite color of green!")


