from fontPens import flattenPen

g = CurrentGlyph()

# Wrap this operation in an "undo" step, so you can undo it later.
with g.undo("Flatten current glyph"):  
    # Make your glyph only comprised of flat lines
    flattenPen.flattenGlyph(g, 80)
    