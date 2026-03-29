import ezui


class Demo(ezui.WindowController):

    # The build function runs first
    def build(self):
        # Compose the UI instructions
        content = """
        * TwoColumnForm         @form

        > : Font 0:
        > (Font 0 ...)          @font0
        > : Font 1:
        > (Font 1 ...)          @font1
        
        > : Factor:
        > [_0_]                 @factor
        
        (Generate)              @button
        """
        # Store the font objects and their original ordering upfront
        self.fonts = AllFonts()
        # Set some styling for the things you put in content 
        descriptionData=dict(
            form=dict(
                titleColumnWidth=60,
                itemColumnWidth=220,
            ),
            factor=dict(
                valueWidth=60,
                valueType="float",
                valueIncrement=0.1,
            ),
            button=dict(
                width="fill"
            ),
        )
        # Make the window object itself, put all the stuff in it
        self.w = ezui.EZWindow(
            content=content,
            descriptionData=descriptionData,
            defaultButton="button",
            controller=self
        )
        # Loop through each of the dropdown identifiers
        for identifier in ["font0", "font1"]:
            # Get the UI element
            drop_down = self.w.getItem(identifier)
            # Add some strings representing the fonts to the list
            items = [f.info.familyName + " " + f.info.styleName for f in self.fonts]
            drop_down.setItems(items)
            # For the second dropdown, change the selection to the second font (if there is more than one font open)
            if identifier == "font1" and len(self.fonts) > 1:
                drop_down.set(1)

    # The started function runs second
    def started(self):
        # Open the window
        self.w.open()
        
    # Choose what happens when you press the button
    def buttonCallback(self, sender):
        print("Button pressed!")
        # Create a new_font
        new_font = RFont(showInterface=False)
        # Get the font from the first dropdown
        min_font = self.fonts[self.w.getItem("font0").get()]
        # Get the font from the second dropdown
        max_font = self.fonts[self.w.getItem("font1").get()]
        # (Optional) Check if they are interpolable (FYI: this function is not perfect, so don't rely on it usually.)
        compatible = min_font.isCompatible(max_font)
        if not compatible:
            print("Not compatible!")
        else:
            print("Compatible!")
            # Interpolate
            new_font.defaultLayer.name = min_font.defaultLayer.name
            new_font.interpolate(self.w.getItem("factor").get(), min_font, max_font)
            new_font.glyphOrder = min_font.glyphOrder
            # Open the font
            new_font.openInterface()

Demo()