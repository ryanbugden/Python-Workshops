all_fonts = AllFonts()

# You could do it on the Current Glyph, or just type the name here
current_glyph = CurrentGlyph()
print(current_glyph.name)

for font in all_fonts:
    # Get the glyph object from other fonts open
    this_glyph = font[current_glyph.name]
    # Move only the contours
    for contour in this_glyph.contours:
        contour.moveBy((0, 400))