from random import randint

jostle_amount = 200

# Get all fonts
all_fonts = AllFonts()

for font in all_fonts:
    for glyph in font:
        with glyph.undo():
            # Loop through the contours
            for contour in glyph.contours:
                # Loop through the points in each contour
                for point in contour.points:
                    # On each point, move it a random distance.
                    point.x += randint(-jostle_amount, jostle_amount)
                    point.y += randint(-jostle_amount, jostle_amount)
