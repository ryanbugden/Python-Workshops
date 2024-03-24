font = CurrentFont()
glyphs_to_change = ("A", "B", "C", "D")

# Loop through each name
for name in glyphs_to_change:
    # Get the glyphs with those names
    glyph = font[name]
    # Set up a new name
    new_name = name + ".alt"
    # Add the glyph
    font.insertGlyph(glyph, new_name)
    # Get that glyph object
    new_glyph = font[new_name]
    # Move the glyph
    new_glyph.moveBy((0, 400))
    
# # ALTERNATIVELY...
# for name in glyphs_to_change:
#     glyph = font[name]
#     # Make a copied glyph floating in the air, waiting for a home
#     copied_glyph = glyph.copy()
#     copied_glyph.moveBy((0, 400))
#     font.insertGlyph(copied_glyph, name + ".alt")

    