# Get the current font
f = CurrentFont()

# Loop through every layer in the font’s layers
for layer in f.layers:
    # Print the layer object
    print(layer)
    # Loop through every glyph in that object
    for glyph in layer:
        # Set up an undo state in the glyph
        with glyph.undo():
            # Rotate the glyph
            glyph.rotateBy((180))