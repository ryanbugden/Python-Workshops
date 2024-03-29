# Using it right here and now
font = CurrentFont()
print(font.info.styleName)

# Opening it from a path
my_font = OpenFont(
            '/Users/Ryan/Documents/Git/public/Python Workshops/_test_UFOs/Source_Serif_Caption-Bold.ufo', 
            showInterface=False
            )
print(font.info.styleName)