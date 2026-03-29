font = CurrentFont()
glyph_name = "p"

# Get the font layers
foreground = font.defaultLayer
background = font.getLayer("background")
destination = font.getLayer("output")

# Get the two glyph objects
foreground_glyph = foreground[glyph_name]
background_glyph = background[glyph_name]

# Make an empty glyph
new_glyph = RGlyph()

# Interpolate the two glyphs into the empty glyph object
# Interpolation between 0 and 1.
new_glyph.interpolate(0.7, foreground_glyph, background_glyph)

# Put the glyph in the layer
destination.insertGlyph(new_glyph, glyph_name)
