
# ----SUBJECTIVE---
# Choose suffix to append name with
suffix = ".alt"

# ----OBJECTIVE---
# Get the font object
font = CurrentFont()

# Loop through each selected glyph names
for glyph_name in font.selectedGlyphNames:
    # Get their glyph objects with their glyph names
    glyph = font[glyph_name]
    # Append glyph to font
    font.insertGlyph(glyph, name=glyph_name + suffix)
