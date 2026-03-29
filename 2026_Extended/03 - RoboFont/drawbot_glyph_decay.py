# drawBot

# Make a function that draws glyphs with BezierPaths
def draw_glyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)
    
def mess_up_glyph(glyph):
    with glyph.undo("Points!!!!"):
        for contour in glyph.contours:
            for point in contour.points:
                if point.type == "offcurve":
                    point.moveBy((randint(-100, 100), randint(-100, 100)))
    
glyph = CurrentGlyph()
glyph_copy = glyph.copy()

for page_number in range(50):
    newPage()
    glyph_copy.decompose()
    mess_up_glyph(glyph_copy)
    draw_glyph(glyph_copy)
    
saveImage("glyph_decay.gif")