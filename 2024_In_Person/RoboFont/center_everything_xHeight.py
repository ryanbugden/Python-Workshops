
font = CurrentFont()

for glyph in font:
    if not glyph.bounds:
        continue
    left, bottom, right, top = glyph.bounds
    mid_y = (top + bottom) / 2
    desired_mid_y = glyph.font.info.xHeight / 2
    move_y_by = desired_mid_y - mid_y

    # print("Middle of my contour", mid_y)
    # print("Middle of x-height", desired_mid_y)
    # print("How much I want to move it", move_y_by)

    for contour in glyph.contours:
        contour.moveBy((0, move_y_by))