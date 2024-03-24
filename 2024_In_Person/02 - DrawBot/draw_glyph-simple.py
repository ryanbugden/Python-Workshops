# To work with UFOs, we need FontParts
from fontParts.world import RFont

# Make a function that draws glyphs with BezierPaths
def draw_glyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)

# Get the font object, by means of file path
font = RFont('../../_test_UFOs/Source_Serif_Caption-Bold.ufo')

# Use our function to draw the glyph
draw_glyph(font["a"])