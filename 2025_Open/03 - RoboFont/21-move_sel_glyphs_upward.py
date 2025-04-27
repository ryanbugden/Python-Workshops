# menuTitle: Move Selected Glyphs Upward


# ————— SUBJECTIVE —————

# Decide how many units you’d like to move glyphs up
move_y = 100


# ————— OBJECTIVE —————

# Get the font object
font = CurrentFont()
# Get the selected glyph names
selected_glyph_names = font.selectedGlyphNames
# Loop through each of the selected glyph names
for glyph_name in selected_glyph_names:
    # Get their glyph objects using their glyph names
    glyph = font[glyph_name]
    # Store what you're about to do in an "undo"
    with glyph.undo(f"Move {glyph_name} up"):
        # Move the glyphs up!
        # First print a note to self
        print(f"Moving {glyph_name} up!")
        # Only move components if their base glyph isn’t in the selection
        for component in glyph.components:
            if component.baseGlyph not in selected_glyph_names:
                component.moveBy((0, move_y))
        # Choose which non-component elements you want to move
        elements = glyph.contours + glyph.anchors
        # Move those elements all in one loop :) (They each have moveBy() functions available)
        for element in elements:
            element.moveBy((0, move_y))
            
            