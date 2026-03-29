font = CurrentFont()
slant_amount = 14

# Make a new layer for a different skew you might use to reference your drawing
# This is a copy of the default layer
font.insertLayer(font.defaultLayer, "adjusted_reference")
ref_layer = font.getLayer("adjusted_reference")

# Loop through every glyph
for glyph in font:
    # Ignore glyphs with no contents
    if not glyph.bounds:
        continue
    # Get the mid x
    mid_x = glyph.width / 2
    # Basic slant on the default layer
    with glyph.undo("Slant the default layer glyph"):
        for contour in glyph.contours:
            contour.skewBy((slant_amount, 0), origin=(mid_x, 0))
    ref_glyph = ref_layer[glyph.name]
    with ref_glyph.undo("Slant the reference layer glyph"):
        for contour in ref_glyph.contours:
            # Slanting vertically by half, to take the weight off the bottom left and top right
            contour.skewBy((slant_amount, -slant_amount/2), origin=(mid_x, 0))

# Set the italic angle in font info
font.info.italicAngle = -slant_amount
    
# Center stuff visually in RF, using some built-in RoboFont settings
offset = int((font["o"].angledRightMargin - font["o"].angledLeftMargin)/2)
font.lib['com.typemytype.robofont.italicSlantOffset'] = offset

