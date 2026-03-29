from random import randint

glyph = CurrentGlyph()

# Use a with statement to store and undo in the glyph object
with glyph.undo("SOMETHING COOL HAPPENED"):
    # Anything you do in this indent will be packaged into one undo called "SOMETHING COOL HAPPENED"
    # Loop through every contour in the glyph
    for contour in glyph.contours:
        # Loop through every point in the contour
        for point in contour.points:
            # Move that point horizontally
            point.x += randint(-100, 100)
    