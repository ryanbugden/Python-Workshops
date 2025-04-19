# Get font object, the frontmost open font
font = CurrentFont()

# Set up spacing relationships in a dictionary
spacing_data = {
    "e": ["eacute", "eogonek"],
    "O": ["Oacute", "Oogonek"]
    }
    
# Choose half-x-height as the beam ("ray") height, for setting beam margins
y_position = font.info.xHeight / 2

# Loop through the dictionary
for model_glyph_name, follower_names in spacing_data.items():
    # Get the model glyph object using the glyph name
    model_glyph = font[model_glyph_name]
    # Get the beam left margin of the model glyph, and store it in a variable
    left_margin = model_glyph.getRayLeftMargin(y_position)
    # Loop through every follower name in the list (dict value)
    for follower_name in follower_names:
        # Get the follower glyph object using the glyph name
        follower_glyph = font[follower_name]
        # Make a print statement tell you what's happening
        print("Changing", follower_name, "to ", model_glyph_name) 
        # Set the beam left margin, using the chosen beam height and match to the model left margin
        follower_glyph.setRayLeftMargin(y_position, left_margin)
        # Match the wdith of the model glyph (could also do beam right margin, but this is more reliable)
        follower_glyph.width = model_glyph.width
        