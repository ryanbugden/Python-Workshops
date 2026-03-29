# Import "GetFile" UI goodie from mojo.UI (see RoboFont.com)
from mojo.UI import GetFile


def interpolate_two_fonts(factor, font_1, font_2):
    new_font = RFont()
    new_font.defaultLayer.name = font_1.defaultLayer.name
    new_font.interpolate(factor, font_1, font_2)
    new_font.glyphOrder = font_1.glyphOrder

# Open up a MacOS dialog asking for a selection of two UFOs.
# This will output a list of two paths (strings)
cool_fonts = GetFile(
    message="Select two fonts", 
    title="Interpolate Two Fonts", 
    allowsMultipleSelection=True, 
)
# Use the two paths and get their respective font objects
font_1 = OpenFont(cool_fonts[0], showInterface=False)
font_2 = OpenFont(cool_fonts[1], showInterface=False)
# Run our function to interpolate between them
interpolate_two_fonts((-2, 2), font_1, font_2)
