# menuTitle: Generate Case-Sensitive Punctuation


# Get our font object
font = CurrentFont()

# Establish our suffix 
suffix = ".case"

# Define what characters need a CAPS version as source glyphs
source_glyph_names = ["guilsinglleft", "guilsinglright", "guillemotleft", "guillemotright", "hyphen", "endash", "emdash", "periodcentered", "bullet", "parenleft", "parenright", "bracketleft", "bracketright", "braceleft", "braceright", "slash", "bar", "backslash", "brokenbar", "at"]

# Create new versions with .case name
for glyph_name in source_glyph_names:
    if glyph_name in font.keys():
        source_glyph = font[glyph_name]
        # Copy artwork from source glyph to new glyph
        font.insertGlyph(source_glyph, name=glyph_name + suffix)
        # Capture this new glyph object
        new_glyph = font[glyph_name + suffix]
        # Move artwork to mid-way between base-line and cap-height
        # Calculate the mid_y
        left, bottom, right, top = new_glyph.bounds
        source_mid_y = (top - bottom) / 2 + bottom
        # We know where it needs to go
        destination_mid_y = font.info.capHeight / 2
        # Calculate the difference
        y_diff = destination_mid_y - source_mid_y
        # Move it
        new_glyph.moveBy((0, y_diff))

