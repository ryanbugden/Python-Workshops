from mojo.UI import AskString

font = CurrentFont()

# Choose how much you want to track out each glyph
tracking = int(AskString(title="Change tracking", message="What tracking do you want?", value="10"))
# Make sure this is even
tracking = int(tracking/2) * 2

# Loop through each glyph in the font
for glyph in font:
    # Change the sidebearings according to the choice above
    if glyph.bounds:
        glyph.leftMargin += tracking/2
        glyph.rightMargin += tracking/2
    else:
        glyph.width += tracking