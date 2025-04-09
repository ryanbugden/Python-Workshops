# Get the font
font = CurrentFont()

# Loop through all glyphs in the font
for glyph in font:
    # Set the glyph’s mark color attribute to red
    glyph.markColor = (1, 0, 0, 1)    
    
# Give confirmation that it's finally done
print("Done!")
