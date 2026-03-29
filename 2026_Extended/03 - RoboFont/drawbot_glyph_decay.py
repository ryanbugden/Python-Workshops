# Run in RoboFont’s DrawBot extension

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
    
# Get the current glyph
glyph = CurrentGlyph()
# Make a copy of the glyph that is floating in the abyss!
glyph_copy = glyph.copy()
# Decompose the glyph copy so we don't have to worry about components
glyph_copy.decompose()

# Loop through 50 numbers
for page_number in range(50):
    # Each time, make a new page
    newPage()
    # Run our glyph through our "mess_up_glyph" function
    mess_up_glyph(glyph_copy)
    # And then draw that glyph
    draw_glyph(glyph_copy)
    
# Save multi-page doc as a gif
saveImage("glyph_decay.gif")