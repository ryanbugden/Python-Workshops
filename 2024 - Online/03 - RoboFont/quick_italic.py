# Decide how you want to slant
slant_amount = 25

# Make a function that skews the glyph the way we like it
def skew_glyph(glyph, slant_formula):
    with glyph.undo():
        # Slant only contours
        for contour in glyph.contours:
            contour.skewBy(slant_formula, origin=(glyph.width/2, 0))
        for anchor in glyph.anchors:
            anchor.skewBy(slant_formula, origin=(glyph.width/2, 0))

# Get your font object
font = CurrentFont()
font.newLayer("double_slant_reference")
reference_layer = font.getLayer("double_sl`ant_reference")

# Loop through every glyph in font
for glyph in font:
    # Add that glyph to the other layer
    reference_layer.insertGlyph(glyph, glyph.name)
    # Store the layer glyph in a variable
    that_glyph = reference_layer[glyph.name]
    # Skew the glyph
    skew_glyph(glyph, slant_amount)
    # Skew the background glyph
    skew_glyph(that_glyph, (slant_amount, -slant_amount/2))
    
# Set the font’s italic angle
font.info.italicAngle = -25
