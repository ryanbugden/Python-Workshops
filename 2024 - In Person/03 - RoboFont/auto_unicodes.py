font = CurrentFont()

# Loop through every glyph in the font/
for glyph in font:
    # Auto-assign its unicode, based on its glyph name
    glyph.autoUnicodes()