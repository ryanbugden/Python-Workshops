from random import random

# Get out currently open font
font = CurrentFont()
# Loop through every layer
for layer in font.layers:
    # Loop through every glyph
    for glyph in layer:
        # Set up an undo state in the glyph, so we can undo if we don't like this
        with glyph.undo():
            # Loop through every contour in the glyph
            for my_contour in glyph.contours:
                # Loop through every point in the contour
                for my_point in my_contour.points:
                    # Add a random number from -50 to 50 to x
                    my_point.x += (random()-0.5)*100
                    # Add a random number from -50 to 50 to Y
                    my_point.y += (random()-0.5)*100