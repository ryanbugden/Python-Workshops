# Get the font
font = CurrentFont()

# Loop through the glyph names, in the order you see in Font Overview
for glyph_name in font.glyphOrder:
    # Get the glyph object using the glyph name
    glyph = font[glyph_name]
    