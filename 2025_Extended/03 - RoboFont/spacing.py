all_fonts = AllFonts()

# Set tracking value
tracking = 50

# Loop through each font in all open fonts
for font in all_fonts:
    # Loop through each glyph name in that font’s glyph order
    for glyph_name in font.glyphOrder:
        # Get the glyph object from the glyph name
        glyph = font[glyph_name]
        # Check if there is stuff in the glyph. If so...
        if glyph.bounds is not None:
            # Set the glyph’s left margin to 0
            glyph.leftMargin += tracking / 2
            # Set the glyph’s right margin to 0
            glyph.rightMargin += tracking / 2
        # If the glyph is empty...
        else:
            # Just change the width
            glyph.width += tracking