from mojo.UI import AskString

font = CurrentFont()

# Choose how much you want to track out each glyph
tracking = int(AskString(title="Change Tracking", message="What tracking do you want?", value="10"))

# Make sure this is even
if tracking % 2:
    print("This is not an even number.")
else:
    # Loop through each glyph in the font
    for glyph in font:
        # Change the sidebearings according to the choice above
        if glyph.bounds:
            # Bonus: Does this work if we have components?
            glyph.leftMargin  += tracking/2
            glyph.rightMargin += tracking/2
        # If no content in the glyph, just change the width
        else:
            glyph.width += tracking