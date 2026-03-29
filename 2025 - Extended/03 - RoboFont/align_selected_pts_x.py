glyph = CurrentGlyph()

# First figure out the average x of the selected points
# Get x values of each point
point_xs = []
for point in glyph.selectedPoints:
    point_xs.append(point.x)
# Find the two extremes
min_x = min(point_xs)
max_x = max(point_xs)
# Average them!
average_x = int((min_x + max_x) / 2)

# Use the above to set the x accordingly
with glyph.undo("Align points, Roberto style"):
    for b_point in glyph.selectedBPoints:
        # Get the anchor coordinates
        coord_x, coord_y = b_point.anchor
        print(coord_x, coord_y)
        # Change the x part
        b_point.anchor = (average_x, coord_y)