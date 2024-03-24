glyph = CurrentGlyph()

with glyph.undo("Move up and to the right."):
    glyph.moveBy((100, 0))
    glyph.moveBy((0, 50))