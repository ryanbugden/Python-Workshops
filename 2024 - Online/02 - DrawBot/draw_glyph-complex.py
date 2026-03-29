# We need FontParts to get into the UFO
from fontParts.world import RFont

w, h = 1000, 1000

# Get the font object
my_font = RFont('../Test UFOs/Source_Serif_Display-Bold.ufo')

# Make a function that draws the glyph object to a BezierPath
def draw_glyph(g):
    bez = BezierPath()
    g.draw(bez)
    drawPath(bez)
    # Draw circles on the on-curves
    for x, y in bez.onCurvePoints:
        fill(1)
        stroke(0)
        # Center the ovals on the point with some radius trickery
        radius = 20
        oval(x - radius/2, y - radius/2, radius, radius)

# Loop through every glyph name in the glyph order
for glyph_name in my_font.glyphOrder:
    # Get the glyph object from the glyph name
    my_glyph = my_font[glyph_name]
    # Temporarily take care of components...
    my_glyph.decompose()
    # Make a new page and set the speed of the animation
    newPage()
    frameDuration(1/20)
    
    # Adjust the position of the glyph (centered on page)
    extra_x_space = w - my_glyph.width
    extra_y_space = h - my_font.info.capHeight
    # Move the glyph up and to the right
    translate(extra_x_space/2, extra_y_space/2)
    
    # Draw the glyph outlines
    fill(None)
    stroke(0)
    strokeWidth(2)
    draw_glyph(my_glyph)
    
    # Draw sidebearing lines
    line((0,0), (0, my_font.info.capHeight + 30))
    line((my_glyph.width, 0), (my_glyph.width, my_font.info.capHeight + 30))
    
    # Add note below showing the margins
    fontSize(20)
    stroke(None)
    fill(0)
    lower_by = 50
    text(str(my_glyph.leftMargin), (0, -lower_by), "center")
    text(str(my_glyph.rightMargin), (my_glyph.width, -lower_by), "center")
    
# You made all those pages! Save them in an animated GIF
saveImage("_output/draw_glyph-complex.gif")
