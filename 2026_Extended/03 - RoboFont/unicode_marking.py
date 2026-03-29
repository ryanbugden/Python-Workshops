# Get a list of all open fonts
all_fonts = AllFonts()

# Go through each font in all of the fonts
for font in all_fonts:
    # Print a header in our output
    print(font.info.styleName.upper(), "glyphs with no unicode:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    # Start an empty list to harvest glyphs with no unicode
    glyphs_with_no_unicode = []
    # Go through each glyph in the font’s default layer
    for glyph in font:
        # Is the glyph has no unicode...
        if glyph.unicode is None:
            # ... mark it red
            glyph.markColor = (1, 0, 0, 1)
            # And add it to our once-empty list
            glyphs_with_no_unicode.append(glyph.name)
    # After looping through every glyph, print the final list from that font
    print(glyphs_with_no_unicode)
    print()