# The font I have open
font = CurrentFont()
# Path to font with good glyph order
path_to_good_font = '/path/to/font.ufo'
# Open the font object with no interface (fast)
good_font = OpenFont(path_to_good_font, showInterface=False)
# Steal the glyph order (including template glyphs)
font.templateGlyphOrder = good_font.templateGlyphOrder