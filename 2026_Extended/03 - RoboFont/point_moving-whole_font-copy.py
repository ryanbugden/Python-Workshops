from random import randint

def mess_up_font(font):
    for glyph in font:
        with glyph.undo("Points!!!!"):
            for contour in glyph.contours:
                for point in contour.points:
                    if point.type == "offcurve":
                        point.moveBy((randint(-100, 100), randint(-100, 100)))
                        
# Get the current font
font = CurrentFont()
# Make a floating copy so we don’t mess up our original
font_copy = font.copy()
# Mess up the copy
mess_up_font(font_copy)
# Open the copy up in RoboFont
font_copy.openInterface()
