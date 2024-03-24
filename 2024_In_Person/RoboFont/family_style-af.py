all_fonts = AllFonts()

for font in all_fonts:
    print(font.info.familyName, font.info.styleName)
    print(font.glyphOrder)