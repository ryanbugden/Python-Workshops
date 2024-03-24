# To work with UFOs, we need FontParts
from fontParts.world import RFont

# Make a function that draws glyphs with BezierPaths
def draw_glyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)
    for point in bez.onCurvePoints:
        radius = 5
        oval(point[0] - radius, point[1]- radius, radius *2, radius *2)

# Get the font object, by means of file path
font = RFont('../Test UFOs/Source_Serif_Display-Bold.ufo')
leftover_top_space = height() - font.info.xHeight

for glyph_name in font.glyphOrder:
    newPage()
    translate(0, leftover_top_space/2)
    fill(None)
    stroke(0)
    glyph = font[glyph_name]
    glyph.decompose()
    leftover_right_space = width() - glyph.width
    translate(leftover_right_space / 2, 0)
    draw_glyph(glyph)



