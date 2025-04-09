from random import randint

glyph = CurrentGlyph()

# Loop through every contour in the glyph
for contour in glyph.contours:
    # Loop through every point in the contour
    for point in contour.points:
        # Filter down to only on-curve points (move, line, curve)
        if point.type != "offcurve":
            print(point.type)
            point.x += randint(-200, 200)
            point.y += randint(-200, 200)