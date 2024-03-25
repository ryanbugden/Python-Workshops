# menuTitle: Make Bad Tabular Figures

f = CurrentFont()
tab_width = f['zero'].width  # The desired width for each glyph

figures = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for g_name in figures:
    g = f[g_name]
    new_g = f.newGlyph(g_name + ".tnum")
    new_g.appendGlyph(g)
    new_g.width = g.width
    
    # If the glyph is narrower than it needs to be,
    if new_g.width < tab_width:
        # Just add an equal amount of space to each side.
        side = (tab_width - new_g.width) / 2
        new_g.leftMargin  += side
        new_g.rightMargin += side
    # If the glyph is wider than it needs to be,
    elif new_g.width > tab_width:
        # Scale (squish) it horizontally.
        scale_factor = tab_width / new_g.width
        new_g.scaleBy((scale_factor, 1))
        new_g.width = tab_width
