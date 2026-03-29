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
            # If statements to triage side-dependent operation
            if side == "left":
                old_margin = target_glyph.leftMargin
                target_glyph.leftMargin = source_glyph.leftMargin
                new_margin = target_glyph.leftMargin
            elif side == "right":
                old_margin = target_glyph.rightMargin
                target_glyph.rightMargin = source_glyph.rightMargin
                new_margin = target_glyph.rightMargin
            # If it changed, flip the switch and print the change.
            if old_margin != new_margin:
                something_changed = True
                print(old_margin, "→", new_margin, "Making", target_glyph_name, "left margin match", source_glyph_name)
                
# If nothing changed, tell the user
if something_changed == False:
    print("💚 You checked everything, and everything is fine")
            
            
        
