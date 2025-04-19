from mojo.UI import SelectFont

tool_title = "Interpolate Two Fonts"

# ==== SUBJECTIVE
# Decide upon a factor
factor = 0.5

# ==== THE PROGRAM
# Create a new_font
new_font = RFont(showInterface=False)
# Get the first font
min_font = SelectFont(message='Select the minimum font:', title=tool_title)
# Get the second font
max_font = SelectFont(message='Select the maximum font:', title=tool_title)
# (Optional) Check if they are interpolable (FYI: this function is not perfect, so don't rely on it usually.)
compatible = min_font.isCompatible(max_font)
if not compatible:
    print("Not compatible!")
else:
    print("Compatible!")
    # Interpolate
    new_font.defaultLayer.name = min_font.defaultLayer.name
    new_font.interpolate(factor, min_font, max_font)
    new_font.glyphOrder = min_font.glyphOrder
    # Open the font
    new_font.openInterface()