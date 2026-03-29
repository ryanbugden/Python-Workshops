# Get the current font
font = CurrentFont()
# Write a list of our oldstyle glyph names, store in a variable
os_names = ["zero.osf", "one.osf", "two.osf", "three.osf", "four.osf", "five.osf", "six.osf", "seven.osf", "eight.osf", "nine.osf"]
# Loop through every glyph name
for os_name in os_names:
    # Get glyph object by selecting the name to the font
    os_glyph = font[os_name]
    os_glyph.markColor = ()
    # Make a new glyph with a similar name + ".lf", that copies the glyph
    new_name = os_name.replace(".osf", ".lf")
    font.insertGlyph(os_glyph, new_name)
    new_glyph = font[new_name]
    # Get the bounds of the new glyph (position and height)
    bottom = new_glyph.bounds[1]
    height = new_glyph.bounds[3] - new_glyph.bounds[1]
    # Move the glyph vertically 
    new_glyph.moveBy((0, -bottom))
    # Calculate the scale factor (cap height / height of the new glyph)
    vertical_scale_factor = font.info.capHeight / height
    # Scale the height of the new glyph (not width)
    new_glyph.scaleBy((1, vertical_scale_factor))
    new_glyph.markColor = (0, 0, 1, 1)