from mojo.tools import IntersectGlyphWithLine

# Define a function to check the case of a string
def check_case(string):
    if string == string.lower():
        return "lowercase"
    else:
        return "uppercase"

# Come up with some sort of script that figures out stem width ;)
# Define a function that gets the stem widths
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
    
    
threshold = 2

# Get the font 
font = CurrentFont()
# Get the stem widths of the H and n
H_stems = get_stem_widths(font['H'])
n_stems = get_stem_widths(font['n'])
# Loop through each glyph of the font (or define specific glyphs to check)
for glyph in font:
    if glyph.unicode:
        case = check_case(chr(glyph.unicode))
    else:
        case = "lowercase"
    stem_widths = get_stem_widths(glyph)
    for stem_width in stem_widths:
        if case == "uppercase":
            # Check it against H stems
            for H_stem in H_stems:
                if stem_width != H_stem and H_stem - threshold < stem_width < H_stem + threshold:
                    glyph.markColor = (1,1,0,1)
                    print("OH NO!", glyph.name, stem_width, "maybe it should be:", n_stem)
        else:
            # Check it against n stems
            for n_stem in n_stems:
                if stem_width != n_stem and n_stem - threshold < stem_width < n_stem + threshold:
                    glyph.markColor = (1,1,0,1)
                    print("OH NO!", glyph.name, stem_width, "maybe it should be:", n_stem)

