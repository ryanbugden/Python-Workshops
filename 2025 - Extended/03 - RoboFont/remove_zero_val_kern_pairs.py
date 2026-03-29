all_fonts = AllFonts()

# Loop through each font in all open fonts
for font in all_fonts:
    # Loop through each kerning pair and kern value in the kerning information
    for pair, value in font.kerning.items():
        # If the kern value is stored but also 0...
        if value == 0:
            print(pair)
            # Delete the pair from the kerning data!
            del font.kerning[pair]