# Import the randint() function to use in the scripts
from random import randint

# Get the current glyph
glyph = CurrentGlyph()

# Set up an undo state in the glyph
with glyph.undo("Points!!!!"):
    # Loop through every contour in the glyph’s list of contours
    for contour in glyph.contours:
        # Loop through every point in the contour’s list of points
        for point in contour.points:
            print(point.type)
            # Move only off-curves
            if point.type == "offcurve":
                point.moveBy((randint(-100, 100), randint(-100, 100)))
