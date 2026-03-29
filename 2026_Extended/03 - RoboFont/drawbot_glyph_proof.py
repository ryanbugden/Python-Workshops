

# Make a function that draws glyphs with BezierPaths
def draw_glyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)
    
font = CurrentFont()
font_copy = font.copy()

for glyph in font_copy:
    newPage()
    glyph.decompose()
    draw_glyph(glyph)
    
saveImage("")