# To work with UFOs, we need FontParts
from fontParts.world import RFont

# Make a function that draws glyphs with BezierPaths
def draw_glyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)
    # Choose a radius for the dots you're about to draw
    dot_radius = 5
    # Loop through all of the Bezier path’s on-curve points
    for point in bez.onCurvePoints:
        # Draw a dot on a point
        oval(point[0] - dot_radius, point[1]- dot_radius, dot_radius * 2, dot_radius * 2)

# Get the font object, by means of file path
font = RFont('../../_test_UFOs/Source_Serif_Caption-Regular.ufo')
# Calculate the space above the glyph. It’s the page height minus the font’s x-height
leftover_top_space = height() - font.info.xHeight

# Loop through every glyph name in the font’s glyph order tuple
for glyph_name in font.glyphOrder:
    # Get the glyph object
    glyph = font[glyph_name]
    # Make a new page for each glyph
    newPage()
    fill(None)
    stroke(0)
    # Decompose the glyph for this script, so we don't have to worry about components
    glyph.decompose()
    # Calculate the space above the glyph. It’s the page height minus the font’s x-height
    leftover_top_space = height() - font.info.xHeight
    # Calculate the space to the right of the glyph. It’s the page width minus this glyph’s width
    leftover_right_space = width() - glyph.width
    # Move the canvas to the right and up
    translate(leftover_right_space / 2, leftover_top_space/2)
    # Draw the glyph, using our function above
    draw_glyph(glyph)


saveImage("_output/glyph_drawing_proof.pdf")
