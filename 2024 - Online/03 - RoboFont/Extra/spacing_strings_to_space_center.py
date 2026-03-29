# menuTitle: Spacing Strings to Space Center

from mojo.UI import CurrentSpaceCenter

f = CurrentFont()

# Start an empty string
text = ''
# Loop through selected glyphs
for g_name in f.selectedGlyphNames:
    # Add  a line for each glyph name
    text += f"HH/{g_name} HH OO/{g_name} OO\\n"
    
# Put the text in the space center
CurrentSpaceCenter().setRaw(text)

