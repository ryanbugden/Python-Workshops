# menuTitle: Add Overshoot Guidelines

# Decide the overshoot
overshoot = 10
# Go to the font level
font = CurrentFont()
# Clear other guidelines
font.clearGuidelines()
# Get the x-height, cap-height, all those values!
dimensions = [font.info.descender, 0, font.info.xHeight, font.info.capHeight, font.info.ascender]
# Loop through each dimension and add overshoot around it
for dimension in dimensions:
    # Check if you should subtract or add
    if dimension <= 0:
        y_value = dimension - 10
    else:
        y_value = dimension + 10
    # Add guidelines to those y-values
    font.appendGuideline(position=(0, y_value))