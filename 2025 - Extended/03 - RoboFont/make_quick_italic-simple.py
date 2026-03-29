# Choose an angle
slant_angle = 15
# Get our font object
font = CurrentFont()
# Copy original font into a new one
new_font = font.copy()
# Loop through all glyphs in this copy of the font
for glyph in new_font:    
    # Skew each contour and anchor in each glyph
    for contour in glyph.contours:    
        contour.skewBy(slant_angle, origin=(glyph.width/2, 0))
    for anchor in glyph.anchors:
        anchor.skewBy(slant_angle, origin=(glyph.width/2, 0))
    # Copy glyph to skewed layer
    glyph.copyToLayer("skewed", clear=True)
    # Fix the glyph width
    glyph.getLayer("skewed").width = glyph.width
# Change font’s italic angle
new_font.info.italicAngle = -slant_angle
new_font.info.styleName = "Italic"
# Actually open the font
new_font.openInterface()
