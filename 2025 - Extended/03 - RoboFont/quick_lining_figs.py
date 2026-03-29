# Establish our font
font = CurrentFont()
# Get only the oldstyle figure glyphs
glyph_names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# Loop through each name
for glyph_name in glyph_names:
    # Get the glyph object
    glyph = font[glyph_name]
    # Make a copy of the glyph
    # Put that in a new glyph (name + ".lnum")
    new_name = glyph_name + ".lnum"
    font.insertGlyph(glyph, name=new_name)
    # Get the new glyph
    new_glyph = font[new_name]
    # Remove unicodes
    new_glyph.unicodes = []
    # Mark it a cool color
    new_glyph.markColor = (1, 1, 0, 1)
    # Get the bounds of the glyph
    left, bottom, right, top = glyph.bounds
    original_height = top - bottom
    # Establish the goal (baseline to cap-height)
    desired_height = font.info.capHeight
    # Calculate vertical scale we need to do
    print(glyph.name, "HEIGHT:", original_height, "GOAL:", desired_height)
    vertical_scale = desired_height / original_height
    # Calculate position difference
    y_offset = -bottom
    # Reposition
    new_glyph.moveBy((0, y_offset))
    # Scale
    new_glyph.scaleBy((1 ,vertical_scale), origin=(0,0))
