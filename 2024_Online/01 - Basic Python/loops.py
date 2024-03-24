list_of_glyphs = ["A", "A.alt", "B", "B.alt", "B.ss01"]

# Loop through every glyph name in your list of glyphs
for super_cool_glyph_name in list_of_glyphs:
    # Store it in another variable if you want, who cares!
    new_variable_name_whatever = super_cool_glyph_name
    print(new_variable_name_whatever.upper())
print()  # Prints an empty line

string = "ABCD"
# Loop through every character in a string
for pizza_pizza in string:
    print(pizza_pizza)
print()
    
# Dictionary of contour counts
dict_of_glyphs = {
    "A"    : 2, 
    "A.alt": 3
    }
# Looping through dictionary.items(), which formats the dictionary as a list of tuples of two
for glyph_name, contour_count in dict_of_glyphs.items():
    if contour_count == 2:
        print(glyph_name)
        