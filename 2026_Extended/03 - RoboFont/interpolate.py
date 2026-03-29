# Make a function that takes a factor and two fonts, and interpolates them
def interpolate_two_fonts(factor, font_1, font_2):
    # Make a new empty font
    new_font = RFont()
    # Match the default layer of the new font to the first font, to make sure we have the same layer setup
    new_font.defaultLayer.name = font_1.defaultLayer.name
    # Make the new font into an interpolation of the other two
    new_font.interpolate(factor, font_1, font_2)
    # Set the glyph order of the new font to the glyph order of the first one
    new_font.glyphOrder = font_1.glyphOrder


# Get the minimum font object by file path
cool_minimum_font = OpenFont(
    '../../_test_UFOs/Source_Serif-Caption_Thin.ufo',
    showInterface=False
)
# Get the maximum font object by file path
cool_maximum_font = OpenFont(
    '../../_test_UFOs/Source_Serif-Caption_Black.ufo',
    showInterface=False
)
# Run our function with those inputs
interpolate_two_fonts((-2, 2), cool_minimum_font, cool_maximum_font)
