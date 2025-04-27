from random import randint
from mojo.subscriber import Subscriber, registerGlyphEditorSubscriber


# Make a scubsriber object
class MyCoolSubscriber(Subscriber):

    # Build is the function that is run as soon as this 
    # Glyph Editor Subscriber starts (when a glyph editor is opened)
    def build(self):
        self.glyph = None
        print("A glyph editor just opened!")
        print("Anything I do here will happen when a glyph editor is opened.")
        
    ## This would be a function if you want something to happen when the mouse drags.
    # glyphEditorDidMouseDragDelay = 0
    # def glyphEditorDidMouseDrag(self, info):
    #     glyph = info['glyph']
    #     x, y = info['deviceState']['locationInWindow']
    #     print(x, y)
    #     left, bottom, right, top = glyph.bounds
    #     target_left = -x
    #     target_bottom = -y
    #     x_diff = target_left - left
    #     y_diff = target_bottom - bottom
    #     glyph.moveBy((x_diff, y_diff))
    
    # Latch onto when right click happens in this glyph editor
    def glyphEditorWantsContextualMenuItems(self, info):
        # Store the glyph object as an attribute of the Subscriber object
        self.glyph = info["glyph"]
        # Add menu items with some callbacks
        menu_items = [
            ("Move glyph up", self.option1Callback),
            ("Move glyph down", self.option2Callback),
        ]
        info["itemDescriptions"].extend(menu_items)
        
    # Choose what the callbacks do
    def option1Callback(self, sender):
        print("You just selected Option 1!")
        self.glyph.moveBy((0, 200))
        
    def option2Callback(self, sender):
        print("You just selected Option 2!")
        self.glyph.moveBy((0, -200))
    

# Inject that subscriber template you made
registerGlyphEditorSubscriber(MyCoolSubscriber)