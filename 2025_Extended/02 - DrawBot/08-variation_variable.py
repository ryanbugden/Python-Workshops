# Set a file path to your variable font
font_path = '/path/to/variable/font.ttf'

width = 1000
height = 1000
newPage(width, height)

Variable([
    # Create a variable called 'weight_value'
    # and make a slider UI for it.
    dict(
        name="weight_value", 
        ui="Slider",
        args=dict(
            value=100,
            minValue=100,
            maxValue=900
            ),
    )], 
    globals()
    )

# Set the font to the variable font
font(font_path)
# Set the variable font axis to the slider value
fontVariations(wght=weight_value)
# Set a big font size
fontSize(700)
# Draw some text in the middle of the page
text("a", (width/2, height/3), align="center")