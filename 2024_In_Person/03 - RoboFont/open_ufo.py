from mojo.UI import GetFile

path = GetFile(
            message="Choose a UFO file", 
            title="UFO Picker", 
            directory=None, 
            allowsMultipleSelection=False, 
            fileTypes=["ufo"],
            )
            
OpenFont(path)