from mojo.UI import AskString, AskYesNoCancel


# Ask for the glyph name in a pop-up window
my_output = AskString("Write a glyph name to mark yellow", value='A', title='Mark glyph')
# Ask for yes/no confirmation
yes_no_option = AskYesNoCancel("Do you want to mark it?????", title='Intro to Python', default=0, informativeText='')

# Only run the script if user selected Yes
if yes_no_option == 1:
    font = CurrentFont()
    # Get the glyph object from a given glyph name
    my_glyph = font[my_output]
    # Change the glyph’s mark color
    my_glyph.markColor = (1, 1, 0, 0.8)

