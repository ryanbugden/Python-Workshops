# Get the current font
font = CurrentFont()
# Get the first glyph I’m interested in (leader)
leader_glyph = font["n"]
print(leader_glyph)
# Get the second glyph I'm interested in (follower)
follower_glyph = font["h"]
print(follower_glyph)
# Set the right sidebearing of the second glyph to be the same as the first
follower_glyph.rightMargin = leader_glyph.rightMargin