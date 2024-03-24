# One dictionary of contour counts
my_dict = {
    "A"    : 2, 
    "A.alt": 3
    }
    
# A separate dictionary of contour counts
other_dict = {
    "B"    : 10, 
    "B.alt": 11
    }

# Define function where you can find a glyph with a certain amount of contours
def find_glyph_with_n_contours(dict_of_glyphs, number):    
    # Looping through dictionary
    for glyph_name, contour_count in dict_of_glyphs.items():
        if contour_count == number:
            print(glyph_name)
        else:
            print("Not found")
        
# Finally run the function, once one each dictionary
find_glyph_with_n_contours(my_dict, 2)
find_glyph_with_n_contours(other_dict, 10)