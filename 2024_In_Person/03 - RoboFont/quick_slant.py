import math

font = CurrentFont()

slant_amount = 14

glyphs_just_x  = ("i", "j", "m", "n")

# Loop through every glyph
for glyph in font:
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
            if glyph.name in glyphs_just_x:
                contour.skewBy((slant_amount, 0), origin=(mid_x, mid_y))
            else:
                contour.skewBy((slant_amount, -slant_amount/2), origin=(mid_x, mid_y))
                
font.info.italicAngle = -slant_amount
    
# centering stuff
my_o = font["o"]
offset = int((my_o.angledRightMargin - my_o.angledLeftMargin)/2)
font.lib['com.typemytype.robofont.italicSlantOffset'] = offset

