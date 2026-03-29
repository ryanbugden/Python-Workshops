# Import some Space Center related things from mojo.UI (see on RoboFont.com)
from mojo.UI import OpenSpaceCenter, CurrentSpaceCenterWindow

# Get all open fonts, and multiple the list to be 10x as long.
all_fonts = AllFonts() * 10

# Loop through all of that list
for font in all_fonts:
    # Open a Space Center for that fonr
    sc = OpenSpaceCenter(font)
    # Set the text happy birthday
    sc.setRaw("Happy\\nBirthday\\nFrancine")
    # Close the window
    CurrentSpaceCenterWindow().close()