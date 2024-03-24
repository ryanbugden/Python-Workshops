from mojo.UI import CurrentSpaceCenter
# Get the font
font = CurrentFont()
# Get the text in Space Center
space_center = CurrentSpaceCenter()
my_text = space_center.getRaw()

# Make an empty glyph
new_glyph = RGlyph()
# Start a metaphorical "cursor" to keep track of x position
cursor = 0
# Loop through each letter in the text
for letter in my_text:
    # Get the glyph object for each letter
    glyph_to_add = font[letter]
    # Add it as a component to the new glyph
    new_glyph.appendComponent(baseGlyph=letter, offset=(cursor, 0))
    # Advance the cursor, to inform the above offset
    cursor += glyph_to_add.width
    print(cursor)

# Set the width to where the cursor left off.
new_glyph.width = cursor
# Add the glyph to the font!
font.insertGlyph(new_glyph, my_text)

