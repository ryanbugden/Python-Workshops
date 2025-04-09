from random import randint

glyph = CurrentGlyph()

# Loop through every point in the glyph’s selected points
for point in glyph.selectedPoints:
    # Filter to only on-curves
    if point.type != "offcurve":
        print(point.type)
        point.x += randint(-200, 200)
        point.y += randint(-200, 200)