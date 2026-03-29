# Import EZUI so we can use it
import ezui

# Establish our class, and name it Demo.
# Base it off EZUI’s base window controller.
class Demo(ezui.WindowController):

    # When the Demo is initiated, "build" is run once.
    def build(self):
        # Spell out our content in EZUI syntax
        content = """
        * TwoColumnForm     @form

        > : Slider Label:
        > ---X--- [_ _]     @slider
        """
       
        descriptionData = dict(
             # Choose how wide our two columns are in the form
            form=dict(
                titleColumnWidth=90,
                itemColumnWidth=300
            ),
             # Choose the min and max values for the slider
            slider=dict(
                minValue=0,
                maxValue=CurrentFont().info.xHeight,
            ),
        )
        # Initiate our window object
        self.w = ezui.EZWindow(
            content=content,
            descriptionData=descriptionData,
            controller=self,
            size="auto"
        )

    def started(self):
        # Actually open our window
        self.w.open()

    def sliderCallback(self, sender):
        # When the slider changes, this function is called.
        # Get the current glyph
        glyph = CurrentGlyph()
        # Move the bottom of the glyph to where the slider says to
        bottom = glyph.bounds[1]
        desired_bottom = sender.get()
        glyph.moveBy((0, desired_bottom - bottom))
        

Demo()