# menuTitle: Make New UFOs From Layers

f = CurrentFont()

for l in f.layers:
    new_f = NewFont()
    new_f.insertLayer(l)
    new_f.glyphOrder = f.glyphOrder
