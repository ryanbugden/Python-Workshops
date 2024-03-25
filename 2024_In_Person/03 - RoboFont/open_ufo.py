# Import a library to help you pull up a get-file window
from mojo.UI import GetFile

# Store the selected file path as a variable
path = GetFile(
            message="Choose a UFO file", 
            title="UFO Picker", 
            directory=None, 
            allowsMultipleSelection=False, 
            fileTypes=["ufo"],
            )
# Open that UFO
OpenFont(path)