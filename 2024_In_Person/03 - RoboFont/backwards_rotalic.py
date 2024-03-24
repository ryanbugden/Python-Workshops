
font = CurrentFont()

def get_mid_y(glyph):
    left, bottom, right, top = glyph.bounds
    mid_y = (top + bottom) / 2
    return mid_y

for glyph in font:
    if not glyph.bounds:
        continue
    mid_y = get_mid_y(glyph)

    with glyph.undo():
        for contour in glyph.contours:
            contour.rotateBy(45, (glyph.width/2, mid_y))
    
        mid_y = get_mid_y(glyph)
        if glyph.name.title() == glyph.name:
            desired_mid_y = glyph.font.info.capHeight / 2
        else:
            desired_mid_y = glyph.font.info.xHeight / 2
        move_y_by = desired_mid_y - mid_y
    
        for contour in glyph.contours:
            contour.moveBy((0, move_y_by))
    