# menuTitle: Mark Glyph Name Green

from mojo.UI import AskString

# Pop up a window asking for a string, store it in variable "glyph_name"
glyph_name = AskString(
    "Which glyph would you like to mark?", 
    value='eight', 
    title='Mark GLYPH!!!'
)
# Get the current font
font = CurrentFont()
# Get the glyph object using the glyph name the user provided
glyph = font[glyph_name]
# Set the mark color of that glyph green
glyph.markColor = (0,0,1,1)