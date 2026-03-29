# menuTitle: Fix Spacing Using Leaders and Followers

leaders_and_followers = {
    "left": {
        "n": ["r"],
        "o": ["c", "d"],
    },
    "right": {
        "n": ["h", "m"],
        "o": ["b"],
    }
}


# Get the current font
font = CurrentFont()
# Loop through the two items in the main dict
for side, connections in leaders_and_followers.items():
    # Loop through each leader and list of followers in the second nested dictionary
    for leader_name, follower_names in connections.items():
        leader_glyph = font[leader_name]
        for follower_name in follower_names:
            follower_glyph = font[follower_name]
            # Depending on the side, match that sidebearing to the leader’s
            if side == "right":
                follower_glyph.angledRightMargin = leader_glyph.angledRightMargin
            elif side == "left":
                follower_glyph.angledLeftMargin = leader_glyph.angledLeftMargin