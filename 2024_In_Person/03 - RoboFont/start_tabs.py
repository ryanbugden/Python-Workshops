font = CurrentFont()

def monospace_glyph(glyph, desired_width):
    current_width = glyph.width
    difference = desired_width - current_width
    amount_to_each_sb = difference / 2
    
    with glyph.undo():
        # If there are contours
        if glyph.bounds:
            glyph.leftMargin += amount_to_each_sb
            glyph.rightMargin += amount_to_each_sb
        # If it's empty
        else:
            glyph.width = desired_width
        # If it's too wide
        if amount_to_each_sb < 0:
            # Mark red because it's squished.
            glyph.markColor = (1, 0, 0, 0.5)
            scale_x = desired_width / current_width
            glyph.scaleBy((scale_x, 1), origin=(glyph.width/2, 0))
        # If you had to add a lot of space, mark it blue
        elif amount_to_each_sb > 100:
            glyph.markColor = (0, 0, 1, 0.5)


desired_width = font["zero"].width
suffix = ".tab"

for glyph_name in font.selectedGlyphNames:
    my_glyph = font[glyph_name]
    font.insertGlyph(my_glyph, glyph_name + suffix)
    new_glyph = font[glyph_name + suffix]
    monospace_glyph(new_glyph, desired_width)

    