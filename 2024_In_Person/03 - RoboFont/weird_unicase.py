# menuTitle: Stretch All Glyphs Into Cap Area

font = CurrentFont()

# Loop through every glyph
for glyph in font:
    if not glyph.bounds:
        continue
    # Get the height, and figure out how much you need to scale it vertically
    left, bottom, right, top = glyph.bounds
    height = top - bottom
    desired_height = font.info.capHeight
    y_scale = desired_height / height
    
    with glyph.undo():
        # Scale the glyph vertically
        glyph.scaleBy((1, y_scale), origin=(glyph.width / 2, 0))
        # Move it vertically back to baseline
        glyph.moveBy((0, -glyph.bounds[1]))
    