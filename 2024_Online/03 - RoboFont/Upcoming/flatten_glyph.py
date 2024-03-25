from fontPens import flattenPen

g = CurrentGlyph()

with g.undo("Flatten current glyph"):  # Wrap this operation in an "undo" step, so you can undo it later.
    flattenPen.flattenGlyph(g, 80)
    