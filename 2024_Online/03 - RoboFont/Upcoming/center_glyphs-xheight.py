# menuTitle: Center Glyphs Vertically Against X-Height

f = CurrentFont()

for g_name in f.selectedGlyphNames:
    g = f[g_name]

    l, b, r, t = g.bounds
    height_diff = f.info.xHeight - (t - b)
    move_y = (height_diff / 2) - b
    g.moveBy((0, move_y))
    