from random import randint
from mojo.subscriber import Subscriber, registerFontOverviewSubscriber


# Make a template subscriber object
class MySubscriber(Subscriber):
    
    # Hook onto when the user right clicks on the font overview
    def fontOverviewWantsContextualMenuItems(self, info):
        # Get the glyph object from the info dictionary that Subscriber provides (built in argument)
        glyph = info["glyph"]
        # Get the font object, and store it as an attribute "font" for this subscriber
        self.font = glyph.font
        # Set up a list of tuples: menu items and their callbacks
        menu_items = [
            ("MAKE ALT GLYPH!", self.make_alt_glyph_callback)
        ]
        # Add the menu items to the menu
        info["itemDescriptions"].extend(menu_items)
        
    # Add a function that is the callback for when the menu item is clicked
    def make_alt_glyph_callback(self, sender):
        suffix = ".alt"
        # Loop through the selected glyph names of our font
        for glyph_name in self.font.selectedGlyphNames:
            glyph = self.font[glyph_name]
            self.font.insertGlyph(glyph, name=glyph_name + suffix)
    

registerFontOverviewSubscriber(MySubscriber)