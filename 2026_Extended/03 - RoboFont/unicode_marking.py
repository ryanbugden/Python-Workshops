all_fonts = AllFonts()

# Go through each font in all of the fonts
for font in all_fonts:
    print(font.info.styleName.upper(), "glyphs with no unicode:")
    print("===~=~=~=~~==~=~=~~=~=~~=")
    glyphs_with_no_unicode = []
    # Go through each glyph in the default layer
    for glyph in font:
        # Check to see if it doesn't have a unicode
        if glyph.unicode is None:
            # If not, mark it red
            glyph.markColor = (1, 0, 0, 1)
            glyphs_with_no_unicode.append(glyph.name)
    print(glyphs_with_no_unicode)
    print()