# Choose an anisotropic factor by which we interpolate
factor = (1.2, -0.2)
# Get both fonts from their paths (".." goes back a folder. This is a "relative" path.)
min_font = OpenFont(
    '../../_test_UFOs/Source_Serif_Display-Regular.ufo',
    showInterface=False
    )
max_font = OpenFont(
    '../../_test_UFOs/Source_Serif_Display-Regular.ufo',
    showInterface=False
    )
# Make an empty new font
new_font = RFont()
# Interpolate into the new font
new_font.interpolate(factor, min_font, max_font, suppressError=False)
# Correct the glyph order
new_font.glyphOrder = min_font.glyphOrder
# Steal the unicodes from the minimum font
for glyph in new_font:
    glyph.unicodes = min_font[glyph.name].unicodes