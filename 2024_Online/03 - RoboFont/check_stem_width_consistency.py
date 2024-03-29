# Get this cool tool from RoboFont that is basically an invisible measure tool
from mojo.tools import IntersectGlyphWithLine

font = CurrentFont()

# Make a function that measures stem widths
def get_stroke_width(glyph):
    result = IntersectGlyphWithLine(
                        glyph, 
                        ((-10, font.info.xHeight/3), 
                        (glyph.width + 10, font.info.xHeight/3))
                        )
    if result:
        # Stroke width is the difference of the first two x values.
        stroke_width = abs(result[0][0] - result[1][0])
        # Round it to an integer
        return int(stroke_width)
    else:
        # If there are no measurements, return None
        return None

# Get the stem width of the n and H
my_n = font["n"]
my_H = font["H"]
n_width = get_stroke_width(my_n)
H_width = get_stroke_width(my_H)

# Choose threshold
threshold = 4

# Loop through every glyph in the font
for glyph in font:
    # Get the stem values of those glyphs
    width = get_stroke_width(glyph)
    if width:
        # If the stem values are close but not the same, tell me
        if n_width - threshold < width < n_width + threshold:
            if width != n_width:
                # Make a helpful printout
                print("n:", width, n_width, glyph.name)
                # Mark the potential glyphs to address
                glyph.markColor = (1,0,0,1)
        if H_width - threshold < width < H_width + threshold:
            if width != H_width:
                print("H:", width, H_width, glyph.name)
                glyph.markColor = (1,0,0,1)
                
