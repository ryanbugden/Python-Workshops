from fontParts.world import RFont

# Get a font object
my_font = RFont('../../_test_UFOs/Source_Serif_Caption-Bold.ufo')

# Get a glyph object from font
my_a_glyph = my_font["a"]
# Tell me how many contours this glyph has
print(len(my_a_glyph.contours))

# Make an empty Bezier path
path = BezierPath()
print(path.onCurvePoints)

# Draw the glyph object into the Bezier path
my_a_glyph.draw(path)
# Tell me the off-curves, for kicks.
print(path.offCurvePoints)

# Finally, draw it!
drawPath(path)