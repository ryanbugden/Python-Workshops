from random import randint

def mess_up_font(font):
    for glyph in font:
        with glyph.undo("Points!!!!"):
            for contour in glyph.contours:
                for point in contour.points:
                    if point.type == "offcurve":
                        point.moveBy((randint(-100, 100), randint(-100, 100)))
                        
font = CurrentFont()
mess_up_font(font)
