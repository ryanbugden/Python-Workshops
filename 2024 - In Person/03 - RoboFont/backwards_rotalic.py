font = CurrentFont()

# Make function that gets the middle y coordinate
def get_mid_y(glyph):
    left, bottom, right, top = glyph.bounds
    mid_y = (top + bottom) / 2
    return mid_y

# Loop through each glyph in the font
for glyph in font:
    if not glyph.bounds:
        continue
    mid_y = get_mid_y(glyph)
    # Set up an undo state
    with glyph.undo():
        # Rotate all contour material by 45, using the middle as the origin point
        for contour in glyph.contours:
            contour.rotateBy(45, (glyph.width/2, mid_y))
    
        # Check out the mid-y again, to try and center it on the appropriate font metric
        top_y = glyph.bounds[3]
        if glyph.name.title() == glyph.name:
            desired_top_y = glyph.font.info.capHeight
        # Caution: Need a condition for glyphs that have ascenders!
        else:
            desired_top_y = glyph.font.info.xHeight
        # Calculate how far to move it vertically
        move_y_by = desired_top_y - top_y
        
        # Move all the contours to adjust the vertical position
        for contour in glyph.contours:
            contour.moveBy((0, move_y_by))
    