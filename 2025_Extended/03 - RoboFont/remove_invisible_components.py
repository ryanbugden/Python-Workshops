# Get the font
font = CurrentFont()
# Loop through each glyph in the font
for glyph in font:
    # Loop through each component in the glyph
    for component in glyph.components:
        # Check to see if the component’s baseGlyph is in the font 
        if component.baseGlyph not in font:
            print(component.baseGlyph + " is not in the font! Removing component.")
            glyph.removeComponent(component)
        # and has stuff in it
        elif not font[component.baseGlyph].bounds:
            print(component.baseGlyph + " is empty! Removing component.")
            # If not, remove the component from the glyph
            glyph.removeComponent(component)
        
