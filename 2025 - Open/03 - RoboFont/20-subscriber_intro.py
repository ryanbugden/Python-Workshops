from random import random
# To use Subscriber, you have to import Subscriber + the specific type of subscriber you want to use
from mojo.subscriber import Subscriber, registerFontOverviewSubscriber


# Make a class that sub-classes Subscriber
class ChangeMarkColorTool(Subscriber):

    # Latch onto the internal "roboFontDidSwitchCurrentGlyph" notification
    def roboFontDidSwitchCurrentGlyph(self, info):
        # Get the glyph object that was swtched to
        glyph = info["glyph"]
        # Change the mark color to a random color
        glyph.markColor = (random(), random(), random(), random())


# Start the Subscriber you made above
registerFontOverviewSubscriber(ChangeMarkColorTool)