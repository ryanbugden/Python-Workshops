from random import randint

font = CurrentFont()

# Establish a maximum distance the randomization can go
max_distance = 50

# Loop through each glyph in the font
for glyph in font:
    # Set up an undo state. Everything under here will be stored under an undo.
    with glyph.undo("Randomize points"):
        # Loop through each contour in the glyph
        for contour in glyph.contours:
            # Loop through each point in each contour
            for point in contour.points:
                # Add or subtract a random amount to the point x
                point.x += randint(-max_distance, max_distance)
                # Add or subtract a random amount to the point y
                point.y += randint(-max_distance, max_distance)