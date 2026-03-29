font = CurrentFont()

# Loop through every glyph in the font
for glyph in font:
    # Ignore empty glyphs
    if not glyph.bounds:
        continue
    
    # Find the center, the desired center, and move the difference
    left, bottom, right, top = glyph.bounds
    mid_y = (top + bottom) / 2
    desired_mid_y = glyph.font.info.xHeight / 2
    move_y_by = desired_mid_y - mid_y

    for contour in glyph.contours:
        contour.moveBy((0, move_y_by))