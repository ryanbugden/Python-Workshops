# To work with UFOs, we need FontParts
from fontParts.world import RFont

# Make a function that draws glyphs with BezierPaths
def draw_glyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)

# Get the font object, by means of file path
f = RFont('../Test UFOs/Source_Serif_Display-Bold.ufo')

# Loop through each glyph name in the glyph order
for g_name in f.glyphOrder:
    # Make a new page for each glyph
    newPage()
    # Get the glyph object
    g = f[g_name]
    # Decompose the glyph
    g.decompose()
    # Use my custom function!
    draw_glyph(g)