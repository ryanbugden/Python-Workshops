leaders_and_followers = {
    "n": ["h", "m"],
    "o": ["b"],
}


# Get the current font
font = CurrentFont()
# Loop through each leader and its corresponding list of follower names
for leader_name, follower_names in leaders_and_followers.items():
    # Get the leader glyph object by selecting it from the font using its glyph name
    leader_glyph = font[leader_name]
    # Loop through every follower name
    for follower_name in follower_names:
        # Get its glyph object
        follower_glyph = font[follower_name]
        # Set the follower’s right margin to the leader’s left margin
        follower_glyph.rightMargin = leader_glyph.rightMargin