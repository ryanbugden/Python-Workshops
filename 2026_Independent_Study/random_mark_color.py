# Bring the useful random function in from the outside universe
from random import random

# Get our currently open font
font = CurrentFont()

# Loop through every glyph in the font
for glyph in font:
    # Generate a random color
    my_random_color = (random(), random(), random(), 0.8)
    # Mark that glyph a color
    glyph.markColor = my_random_color