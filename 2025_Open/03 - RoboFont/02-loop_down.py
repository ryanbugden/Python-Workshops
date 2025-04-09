# Get our fancy random function from outside
from random import randint

# Define our parameter
chaos = 300

# Getting our font object
font = CurrentFont()

# Looping through every layer in the font
for layer in font.layers:
    # through every glyph in the layer
    for glyph in layer:
        # through every contour in the glyph
        for contour in glyph.contours:
            # through every point in the contour
            for point in contour.points:
                # Get some random numbers
                x_change = randint(-chaos, chaos)
                y_change = randint(-chaos, chaos)
                # Move the point
                point.moveBy((x_change, y_change)
    