font = CurrentFont()

# Copy the font into the air
copied_font = font.copy()
# Delete all glyphs except for "A"
for glyph in copied_font:
    if glyph.name != "A":
        copied_font.removeGlyph(glyph.name)
# Open the copied font
copied_font.openInterface()

