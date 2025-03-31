# menuTitle: Match Sidebearings

def match_sidebearing(source_glyph, dest_glyph, side="left"):
    # A function to match sidebearings!
    if side == "left":
        dest_glyph.angledLeftMargin = source_glyph.angledLeftMargin
    elif side == "right":
        dest_glyph.angledRightMargin = source_glyph.angledRightMargin
        
        
def match_sidebearing_at_y(source_glyph, dest_glyph, y, side="left"):
    # A function to match sidebearings using a beam or ray at a specific height!
    if side == "left":
        value = source_glyph.getRayLeftMargin(y)
        dest_glyph.setRayLeftMargin(y, value)
    elif side == "right":
        value = source_glyph.getRayRightMargin(y)
        dest_glyph.setRayRightMargin(y, value)

# Get the current font
font = CurrentFont()

# Set the left sidebearing of the font’s "d" to match "o"
match_sidebearing(font["o"], font["d"], side="left")

# Set the "beam" or "ray" left sidebearing of "B" to match "H"
y = font.info.capHeight / 2
match_sidebearing_at_y(font["H"], font["B"], y, side="left")