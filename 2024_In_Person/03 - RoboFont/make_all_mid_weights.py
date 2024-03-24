interpolations = {
            "Medium": 0.1,
            "Semibold": 0.3,
            "Bold": 0.5,
            "Extrabold": 0.6,
            "Black": 0.8,
            }

all_fonts = AllFonts()
first_font = all_fonts[0]
second_font = all_fonts[1]
print(first_font.path)
for style_name, factor in interpolations.items():
    # Make a new empty font object, but don't open it yet.
    new_font = NewFont(showInterface=False)
    # Make the empty font object be an interpolation of the 1st and second
    new_font.interpolate(factor, first_font, second_font)
    # Set the correct glyph order
    new_font.glyphOrder = first_font.glyphOrder
    new_font.info.familyName = first_font.info.familyName
    new_font.info.styleName = style_name
    # Save the font file
    new_font.save(first_font.path.replace("Regular", style_name))


