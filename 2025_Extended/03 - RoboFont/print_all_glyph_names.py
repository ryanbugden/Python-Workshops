# Get the frontmost active font
font = CurrentFont()

# Loop through each glyph in the font
for glyph in font:
    # Print its name
    print(glyph.name)