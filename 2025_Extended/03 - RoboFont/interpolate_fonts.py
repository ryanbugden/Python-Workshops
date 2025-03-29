# Choose a factor by which we interpolate
factor = 0.5
# Get both fonts
all_fonts = AllFonts()
min_font = all_fonts[0]
max_font = all_fonts[1]
# Make an empty new font
new_font = RFont()
# Interpolate into the new font
new_font.interpolate(factor, min_font, max_font)
new_font.glyphOrder = min_font.glyphOrder