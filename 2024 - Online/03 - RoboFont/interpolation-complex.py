# Set up some info
new_weights = {
            0.2: "Book",
            0.4: "Medium",
            0.6: "Semibold"
        }

# Get the two UFOs as font objects
all_fonts = AllFonts()
font_1 = all_fonts[0]
font_2 = all_fonts[1]

for factor, style_name in new_weights.items():
    # Make an empty, floating-in-mid-air font object
    new_font = RFont(showInterface=False)
    # Interpolate the two UFOs into the empty font object
    new_font.interpolate(factor, font_1, font_2)
    # Set the glyph order correctly
    new_font.templateGlyphOrder = font_1.templateGlyphOrder
    # Option to save the font, with a different file name each time
    destination = f'../../_test_UFOs/{font_1.info.familyName}-{style_name}.ufo'
    new_font.save(destination)