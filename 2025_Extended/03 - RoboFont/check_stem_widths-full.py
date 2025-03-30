from mojo.tools import IntersectGlyphWithLine

# Define a function to check the case of a string
def check_case(glyph):
    # Only try to guess if the glyph has a unicode
    if glyph.unicode:
        # Get the character representation of a glyph (e.g. "percent" -> "%")
        character = chr(glyph.unicode)
        # Check to see if the character is the same as when you make it lowercase to check if it’s lowercase
        if character == character.lower():
            return "lowercase"
        else:
            return "uppercase"
    # Otherwise assume it's lowercase ¯\_(ツ)_/¯
    return "lowercase"

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
    
# Decide upon a threshold within which an error will be raised if the stem doesn't match
threshold = 2

# Get the font 
font = CurrentFont()
# Get the stem widths of the H and n
H_stems = get_stem_widths(font['H'])
n_stems = get_stem_widths(font['n'])
# Loop through each glyph of the font (or define specific glyphs to check)
for glyph in font:
    stem_widths = get_stem_widths(glyph)
    for stem_width in stem_widths:
        # Choose which stems to check against
        if check_case(glyph) == "uppercase":
            # Check it against H stems if uppercase
            check_stems = H_stems
        else:
            # Check it against n stems if lowercase
            check_stems = n_stems
        # Check your stem width against all your reference stems
        for check_stem in check_stems:
            # If your stem width is not the same, but it's within threshold range...
            if stem_width != check_stem and check_stem - threshold < stem_width < check_stem + threshold:
                # Mark the glyph yellow
                glyph.markColor = (1,1,0,1)
                # Raise an error
                print("OH NO!", glyph.name, stem_width, "maybe it should be:", check_stem)
        