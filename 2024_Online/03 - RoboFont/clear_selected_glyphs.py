font = CurrentFont()
selected_glyphs = font.selectedGlyphNames

# Loop through all names of the selected glyphs
for glyph_name in selected_glyphs:
    print(glyph_name)
    # Get the glyph object
    glyph = font[glyph_name]
    # Clear the glyph’s contents
    glyph.clear()
    