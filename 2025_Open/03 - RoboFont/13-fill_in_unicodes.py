all_fonts = AllFonts()

# Lazily get the source font and destination font based on the two frontmost UFOs open in RF.
source_font = all_fonts[0]
dest_font = all_fonts[1]

# Loop through glyphs of the destination font
for dest_glyph in dest_font:
    # Check if it doesn't have a unicode, but other does
    if dest_glyph.name in source_font:
        # Get the equivalent source glyph object using the dest_glyph name
        source_glyph = source_font[dest_glyph.name]
        # Check if the unicodes are missing on destination glyph AND if the source glyph DOES have unicodes
        if dest_glyph.unicodes == () and source_glyph.unicodes != ():
            # If so, tell me!
            print(dest_glyph.name, "glyph is missing a unicode!!!!")
            # .. and set the destination unicodes to be the same as the source glyph unicodes
            dest_glyph.unicodes = source_glyph.unicodes