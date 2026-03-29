all_fonts = AllFonts()

for font in all_fonts:
    # If my style name is None, close the font.
    if font.info.styleName == None:
        font.close()