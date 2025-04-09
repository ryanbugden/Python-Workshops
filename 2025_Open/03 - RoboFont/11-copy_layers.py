# Get our source font, from our UFO path...
source_font = OpenFont(
    '/Users/Ryan/Documents/Git/public/Python Workshops/_test_UFOs/Source_Serif-Display_Thin.ufo', 
    # ... without even needing to open the UFO in RoboFont visually!
    showInterface=False
    )
# Get our destination font, from our UFO path...
dest_font = OpenFont(
    '/Users/Ryan/Documents/Git/public/Python Workshops/_test_UFOs/Source_Serif-Caption_Black.ufo', 
    # ... without even needing to open the UFO in RoboFont visually!
    showInterface=False
    )
    
print("Our source font object is:",  source_font)
print("Our destination font object is:",  dest_font)

# Create background layer in destination font if it doesn't exist, and store the layer object in variable "dest_layer"
dest_layer = dest_font.newLayer("background")
# Loop through glyphs of source font’s default layer
for glyph in source_font:
    # Copy glyphs into dest_layer
    dest_layer.insertGlyph(glyph, glyph.name)

# We need to save to make sure changes are committed, because the UFOs aren't "open"
dest_font.save()