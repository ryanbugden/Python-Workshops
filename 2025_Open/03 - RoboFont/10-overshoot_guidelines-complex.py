# menuTitle: Add Overshoot Guidelines (Complex 1)

# Choose which glyph names you want to look at to determine the overshoot
glyph_names_look_at = ["O", "o"]

all_fonts = AllFonts()

# Loop through each font in the list of all open fonts
for font in all_fonts:
    
    # Determine an overshoot
    for glyph_name in glyph_names_look_at:
        if glyph_name in font and font[glyph_name].bounds:
            overshoot = -font[glyph_name].bounds[1]
            # Once you have an overshoot value, stop looping
            break
    
    # Clear other guidelines
    font.clearGuidelines()
    # Get the x-height, cap-height, all those values! And associate them with names (keys here)
    dimensions = {
        "Descender": font.info.descender, 
        "Baseline": 0, 
        "X-Height": font.info.xHeight, 
        "Cap-Height": font.info.capHeight, 
        "Ascender": font.info.ascender
        }
    # Loop through each name and respective dimensions, and add overshoot around it
    for name, dimension in dimensions.items():
        # Check if you should subtract or add
        if dimension <= 0:
            y_value = dimension - overshoot
        else:
            y_value = dimension + overshoot
        # Add guidelines to those y-values, and assign the name according to how it's set up in the dict
        font.appendGuideline(position=(0, y_value), angle=0, name=name + " Overshoot")