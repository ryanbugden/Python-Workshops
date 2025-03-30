threshold = 20

# Get our font
font = CurrentFont()
# Collect font dimensions in a list
good_ys = [font.info.descender, 0, font.info.xHeight, font.info.capHeight, font.info.ascender]
# Loop through each glyph of the font
for glyph in font:
    # Loop through each anchor of the glyph
    for anchor in glyph.anchors:        
        # Check if the anchor’s y position is in good_ys
        if anchor.y not in good_ys:
            # Check to see if the anchor is within range of one of the good_ys
            # Loop through each good y
            for good_y in good_ys:
                # Check if this anchor y is close
                if good_y - threshold < anchor.y < good_y + threshold:
                    # If it is, then snap it!)
                    print(glyph.name, anchor.y, "Maybe we should snap it to...", good_y)
                    anchor.y = good_y
                    print("I just set the anchor y to", good_y)