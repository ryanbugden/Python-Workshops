glyph = CurrentGlyph()
font = glyph.font
cap_height = font.info.capHeight

with glyph.undo("Move and Rotate, yo!"):
    for contour in glyph.contours:
        print(contour.index)
        print("MOVING!")
        contour.moveBy((100, 100))
        print("ROTATING!")
        contour.rotateBy(180, origin=(glyph.width/2, cap_height/2))