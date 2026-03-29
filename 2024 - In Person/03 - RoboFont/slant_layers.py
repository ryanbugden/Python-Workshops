font = CurrentFont()

# Make a function that slants layers
def slant_layer(layer, x, y):
    # Loop through every glyph
    for glyph in layer:
        if not glyph.bounds:
            continue
        # Get the mid x and y
        left, bottom, right, top = glyph.bounds
        mid_x = glyph.width / 2
        if glyph.name == glyph.name.upper():
            mid_y = font.info.capHeight / 2
        else:
            mid_y = font.info.xHeight / 2
    
        with glyph.undo():
            # Slant the glyphs
            for contour in glyph.contours:
                contour.skewBy((x, y), origin=(mid_x, mid_y))

# Make new layers, overwriting the old ones
font.insertLayer(font.defaultLayer, name="slant_h")
font.insertLayer(font.defaultLayer, name="slant_hv")
font.insertLayer(font.defaultLayer, name="crazy")

# Slant the layers
slant_amount = 14
slant_layer(font.getLayer("slant_h"), slant_amount, 0)
slant_layer(font.getLayer("slant_hv"), slant_amount, -slant_amount/2)
slant_layer(font.defaultLayer, slant_amount, 0)
           