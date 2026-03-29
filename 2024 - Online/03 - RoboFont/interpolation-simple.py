# Choose if you want to save the font or open it
save_font = True

# Get the two UFOs as font objects
all_fonts = AllFonts()
font_1 = all_fonts[0]
font_2 = all_fonts[1]

# Make an empty, floating-in-mid-air font object
new_font = RFont(showInterface=False)
# Interpolate the two UFOs into the empty font object
# Interpolation is between 0 and 1, but you can extrapolate (<0 or >1)
new_font.interpolate(0.5, font_1, font_2)
# Set the glyph order correctly
new_font.templateGlyphOrder = font_1.templateGlyphOrder

if save_font:
    # Save the font to this path. (../ means back one folder from this script)
    destination = '../../_test_UFOs/Cool_Font.ufo'
    new_font.save(destination)
else:
    # Open the font
    new_font.openInterface()

