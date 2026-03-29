all_fonts = AllFonts()

# Loop through every font in all fonts
for font in all_fonts:
    # Print some information about each font
    print(font.info.familyName, font.info.styleName)
    print(font.glyphOrder)