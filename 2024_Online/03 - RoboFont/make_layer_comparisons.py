font = CurrentFont()

# Make dictionary of guide glyphs, and where to copy them
guide_gs_and_stuff = {
                "n": ["h", "i", "m"],
                "o": ["d", "q"]
                }

# Get the two font layer objects of interest
foreground = font.defaultLayer
background = font.getLayer("background")

# Loop through our dictionary of data
for leader, followers in guide_gs_and_stuff.items():
    # Get the leader glyph name (key) and turn it into a glyph object
    leader_glyph = font[leader]
    # Loop through every follower glyph name
    for follower_name in followers:
        # Put the leader glyph in that slot’s background
        background.insertGlyph(leader_glyph, follower_name)
