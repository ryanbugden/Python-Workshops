font = CurrentFont()

# Loop through each glyph name in the glyph order
for glyph_name in font.glyphOrder:
    # Get the glyph object from the font
    glyph = font[glyph_name]
    # Add an A component if it's not the "A" glyph
    if glyph_name != "A":
        glyph.appendComponent("A")