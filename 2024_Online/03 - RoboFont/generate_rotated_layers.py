font = CurrentFont()
# Get foreground
foreground_layer = font.defaultLayer
# Make a new layer named "upside_down"
upside_down_layer = font.newLayer("upside_down")

# Loop through every glyph in the foreground
for glyph in foreground_layer:
    # Copy it into the upside_down layer
    upside_down_layer.insertGlyph(glyph, glyph.name)
    upside_down_glyph = upside_down_layer[glyph.name]
    # Rotate if there are contours
    if upside_down_glyph.contours:
        left, bottom, right, top = upside_down_glyph.bounds
        mid_x = (left + right) / 2
        mid_y = (bottom + top) / 2
        upside_down_glyph.rotateBy(180, origin=(mid_x, mid_y))
        
# Now I have a layer of upside down glyphs!

# Loop through my two layers
for layer_name in ["pizzatime", "upside_down"]:
    layer = font.getLayer(layer_name)
    # Make a copy
    copy = font.copy()
    copy.defaultLayer = layer
    copy.generate("otfcff", f"../Test UFOs/Source_Serif-{layer_name}.otf")
    if layer_name != "pizzatime":
        copy.openInterface()
    
    

    