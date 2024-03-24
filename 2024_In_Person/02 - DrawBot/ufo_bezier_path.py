from fontParts.world import RFont

my_font = RFont('/Users/Ryan/Documents/Git/public/Python Workshops/2024_In_Person/Test UFOs/Source_Serif_Caption-Bold.ufo')

path = BezierPath()
print(path.onCurvePoints)

my_a_glyph = my_font["a"]
print(len(my_a_glyph.contours))

my_a_glyph.draw(path)
print(path.offCurvePoints)

drawPath(path)