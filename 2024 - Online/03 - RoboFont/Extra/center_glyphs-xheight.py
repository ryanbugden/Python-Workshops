# menuTitle: Center Glyphs Vertically Against X-Height

f = CurrentFont()

# Loop through selected glyphs
for g_name in f.selectedGlyphNames:
    g = f[g_name]

    # Get the bounds
    l, b, r, t = g.bounds
    # Find the difference between the middle of the x-height and the middle of the glyph
    height_diff = f.info.xHeight - (t - b)
    move_y = (height_diff / 2) - b
    # Move the glyph (also moves anchors and stuff..)
    g.moveBy((0, move_y))
    