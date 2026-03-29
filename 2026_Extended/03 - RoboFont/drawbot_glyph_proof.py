# Run in RoboFont’s DrawBot extension

# Make a function that draws glyphs with BezierPaths
def draw_glyph(g):
    # Saved state is necessary for DrawBot because otherwise canvas 
    # transformations like "translate" will compound every time they’re run. 
    # So outside of savedState(), the canvas transformation is reset.
    with savedState():
        # Figure out where on the page we want to move the glyph
        margin_x = (1000 - g.width) / 2
        margin_y = (1000 - g.font.info.capHeight) / 2
        translate(margin_x, margin_y)
        # Draw the glyph
        bez = BezierPath()
        g.draw(bez)
        drawPath(bez)
    
# Get the current font
font = CurrentFont()
# Make a copy of the font so we don’t mess up the original!
font_copy = font.copy()

# Loop through every glyph name in this font’s actual glyph order
for glyph_name in font_copy.glyphOrder:
    # Make a new page for each
    newPage()
    # Get the glyph object
    glyph = font_copy[glyph_name]
    # Decompose the glyph so we don't have to worry about components
    glyph.decompose()
    # Draw the glyph on the page
    draw_glyph(glyph)
    
# Save all pages in a multi-page PDF
saveImage("glyph_proof.pdf")