# Get all open fonts
all_fonts = AllFonts()

# Loop through each font in all open fonts
for font in all_fonts:
    # Change the family name and style name
    font.info.familyName = "Beowulf 2"
    font.info.styleName = "Good"