from random import randint

glyph = CurrentGlyph()

with glyph.undo("Points!!!!"):
    for contour in glyph.contours:
        for point in contour.points:
            print(point.type)
            if point.type == "offcurve":
                point.moveBy((randint(-100, 100), randint(-100, 100)))