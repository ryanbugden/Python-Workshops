# Get a list of all of the open fonts
all_fonts = AllFonts()
# Loop through each font
for font in all_fonts:
    print(font)
    # Loop through each layer in the font
    for layer in font.layers:
        # Loop through each glyph in the layer
        for glyph in layer:
            # Check if bounds go above the x-height
            if glyph.bounds is not None and glyph.bounds[3] > font.info.xHeight:
                # If True, change glyph mark color to be green
                glyph.markColor = (0,0,1,1)