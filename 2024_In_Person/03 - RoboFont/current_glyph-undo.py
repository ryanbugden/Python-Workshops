glyph = CurrentGlyph()

# This is how you package things in an undo event.
# Look at the Edit > Undo menu
with glyph.undo("Move up and to the right."):
    glyph.moveBy((100, 0))
    glyph.moveBy((0, 50))