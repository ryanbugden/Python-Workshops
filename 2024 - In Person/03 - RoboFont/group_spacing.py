font = CurrentFont()
# Set up some a leader glyph, and some follower glyphs, for the left sidebearing
left_spacing_relationships = {
                "O": ["C", "G", "Q"],
                "n": ["i"],
                "o": ["c", "d", "e"],
                }

# Loop through that dictionary
for leader_glyph_name, follower_glyph_names in left_spacing_relationships.items():
    # Get the leader glyph object
    leader_glyph = font[leader_glyph_name]
    # Get its left sidebearing
    leader_lsb = leader_glyph.leftMargin
    # Loop through the follower glyphs
    for follower_name in follower_glyph_names:
        # Get the glyph object based on the name
        follower_glyph = font[follower_name] 
        # Set the sidebearing to match the leader glyph
        follower_glyph.leftMargin = leader_lsb