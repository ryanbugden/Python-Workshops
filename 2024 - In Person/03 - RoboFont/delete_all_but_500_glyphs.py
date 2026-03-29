paths = [
    '../../_test_UFOs/Source_Serif_Caption-Bold.ufo', 
    '../../_test_UFOs/Source_Serif_Caption-Regular.ufo', 
    '../../_test_UFOs/Source_Serif_Display-Bold.ufo', 
    '../../_test_UFOs/Source_Serif_Display-Regular.ufo'
    ]
    
for font_path in paths:
    # Get the font object from the path, without needing to open RF
    font = OpenFont(font_path, showInterface=False)
    # Grab the glyph order as a list, not a tuple
    # Start counting glyphs
    count = 0
    # Loop through every name in the glyph order
    for glyph_name in font.glyphOrder:
        # Once you get past 500 glyphs, delete all the others.
        if count > 500:
            # Delete the glyph from the font
            font.removeGlyph(glyph_name)
        count += 1
    # Save the font
    font.save()