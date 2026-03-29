# menuTitle: Make New UFOs From Layers

f = CurrentFont()

# Loop through every layer
for l in f.layers:
    # Make a new empty font
    new_f = NewFont()
    # Put this font’s layer into the new font
    new_f.insertLayer(l)
    # Correct the glyph order
    new_f.glyphOrder = f.glyphOrder
