# menuTitle: HEY THIS IS A COOL EXAMPLE
# shortCut: shift + command + control + o

# Define the data
relationships = {
    "H": {
        "left":  ["B", "D", "E", "F", "M", "N", "I", "K", "L", "P", "R"],
        "right": ["M", "N", "I", "P", "g", "n"],
        },
    "O": {
        "left":  ["G", "Q"],
        "right": ["D", "Q"],
        },
    "n": {
        "left":  ["m", "i"],
        "right": ["m", "h"],
        },
    "o": {
        "left":  ["q", "d"],
        "right": ["b", "p"],
        },
    }
    
## If you want to get the first string in the left side of the "O" part of the dict
## ... and get the glyph object
# print(font[relationships["O"]["left"][0]])

# Get the font object, the frontmost open font
font = CurrentFont()

# Initiate a switch will go off if something changed
something_changed = False
for source_glyph_name, side_data in relationships.items():
    # Get the source glyph object
    source_glyph = font[source_glyph_name]
    for side, target_glyph_names in side_data.items():
        for target_glyph_name in target_glyph_names:
            # Get the target glyph object
            target_glyph = font[target_glyph_name]
            # Use setattr and getattr to get attributes depending on the side. 
            # Read more about setattr and getattr: https://python-seekho.readthedocs.io/en/latest/auto_examples/oop/getattr_setattr.html
            old_margin = getattr(target_glyph, side + "Margin")
            setattr(target_glyph, side + "Margin", getattr(source_glyph, side + "Margin"))
            new_margin = getattr(target_glyph, side + "Margin")
            # If it changed, flip the switch and print the change.
            if old_margin != new_margin:
                something_changed = True
                print(old_margin, "→", new_margin, "Making", target_glyph_name, "left margin match", source_glyph_name)
                
# If nothing changed, tell the user
if something_changed == False:
    print("💚 You checked everything, and everything is fine")
            
            
        
