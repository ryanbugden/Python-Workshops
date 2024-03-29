# menuTitle: Make Bad Monospaced


f = CurrentFont()
mono_width = 600  # The desired width for each glyph

for g in f:
    # If the glyph has stuff in it...
    if g.bounds != None:
        # If the glyph is narrower than it needs to be,
        if g.width < mono_width:
            # Just add an equal amount of space to each side.
            side = (mono_width - g.width) / 2
            g.leftMargin  += side
            g.rightMargin += side
        # If the glyph is wider than it needs to be,
        elif g.width > mono_width:
            # Scale (squish) it horizontally.
            scale_factor = mono_width / g.width
            g.scaleBy((scale_factor, 1))
            g.width = mono_width
    # If the glyph if empty, just change the width.
    else:
        g.width = mono_width
