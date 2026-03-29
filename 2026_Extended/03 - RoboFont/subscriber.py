# Import randint to use in the script
from random import randint 
# Import our Subscriber tools!
from mojo.subscriber import Subscriber, registerGlyphEditorSubscriber


# Make a Subscriber class to turn into an object
class ShapeMover(Subscriber):
    
    # This runs once when injected
    def build(self):
        print(self)
        print("Our subscriber is in, baby!")
        
    # This runs whenever the mouse is being clicked and dragged
    def glyphEditorDidMouseDrag(self, info):
        # Get the the glyph in which the mouse is being dragged, from our info
        glyph = info['glyph']
        # Get the the position where the mouse is being dragged, from our info
        location = info['locationInGlyph']
        # Figure out where to move the glyph based on the given position
        move_x = location.x - glyph.bounds[0]
        move_y = location.y - glyph.bounds[1]
        jitter = 200
        # Move the glyph!
        glyph.moveBy((move_x + randint(-jitter, jitter), move_y + randint(-jitter, jitter)))

# Inject our subscriber into RoboFont
registerGlyphEditorSubscriber(ShapeMover)