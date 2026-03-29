f = CurrentFont()

for layer in f.layers:
    print(layer)
    for glyph in layer:
        with glyph.undo():
            glyph.rotateBy((180))