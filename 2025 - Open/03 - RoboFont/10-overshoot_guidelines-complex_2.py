# menuTitle: Add Overshoot Guidelines (Complex 2)


# Make a function the takes a font object and tries to get an overshoot value of the font.
def get_overshoot(font):
    glyph_names_look_at = ["O", "o"]
    for glyph_name in glyph_names_look_at:
        if glyph_name in font and font[glyph_name].bounds:
            overshoot = -font[glyph_name].bounds[1]
            # Return our output once you have one.
            return overshoot


all_fonts = AllFonts()

for font in all_fonts:
    # Use the function here. Store the output in a variable. Simple!
    overshoot = get_overshoot(font)
    font.clearGuidelines()
    dimensions = {
        "Descender": font.info.descender, 
        "Baseline": 0, 
        "X-Height": font.info.xHeight, 
        "Cap-Height": font.info.capHeight, 
        "Ascender": font.info.ascender
        }
    for name, dimension in dimensions.items():
        if dimension <= 0:
            y_value = dimension - overshoot
        else:
            y_value = dimension + overshoot
        font.appendGuideline(position=(0, y_value), angle=0, name=name + " Overshoot")