# Factor goes from 0 to 1. We're extrapolating by choosing 2!
factor = 2

# Get all the fonts
all_fonts = AllFonts()
# Get the first font
first_font = all_fonts[0]
# Get the second font
second_font = all_fonts[1]
# Make a new empty font object, but don't open it yet.
new_font = NewFont(showInterface=False)
# Make the empty font object be an interpolation of the 1st and second
new_font.interpolate(factor, first_font, second_font)
# Set the correct glyph order
new_font.glyphOrder = first_font.glyphOrder

# Open the font
new_font.openInterface()

