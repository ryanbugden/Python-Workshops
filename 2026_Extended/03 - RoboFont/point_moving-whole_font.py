# Import randint() function to use in the script
from random import randint

# Make a function that randomizes the position of points
def mess_up_font(font):
    for glyph in font:
        # Set up an undo state in the glyph
        with glyph.undo("Mess up points!!!!"):
            # Loop through every contour in the glyph’s list of contours
            for contour in glyph.contours:
                # Loop through every point in the contour’s list of points
                for point in contour.points:
                    # Move only off-curves
                    if point.type == "offcurve":
                        point.moveBy((randint(-100, 100), randint(-100, 100)))
                        
# Get the current font
font = CurrentFont()
# Run our custom function on the font
mess_up_font(font)
