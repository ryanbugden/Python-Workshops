from mojo.tools import IntersectGlyphWithLine

# Define a function that gets the stem width
def get_stem_widths(glyph):
    # Get the glyph’s font
    font = glyph.font
    # Choose where to measure
    y_value = font.info.xHeight / 2
    # Get hit point coordinates
    measurement = IntersectGlyphWithLine(
        glyph, 
        ((0, y_value), (glyph.width, y_value)), 
        canHaveComponent=True, 
        addSideBearings=False
        )    
    # Sort the measurement from left to right
    measurement = sorted(measurement)
    # Get measurements
    stem_widths = []
    # Loop through each hit point in the measure line
    for i, hit_point in enumerate(measurement):
        # Get each even hit point
        if i % 2 != 0:
            right_hit_point = hit_point
            left_hit_point = measurement[i-1]
            # Calculate the stem width
            stem_width = right_hit_point[0] - left_hit_point[0]
            # Store it in all of the stem widths
            stem_widths.append(stem_width)
    return stem_widths
    
g = CurrentGlyph()
print(get_stem_widths(g))