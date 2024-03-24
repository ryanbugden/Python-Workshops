path = '/Users/Ryan/Documents/Git/public/Python Workshops/2024_In_Person/Test UFOs/Source_Serif_Display-Regular.ufo'
font = OpenFont(path, showInterface=False)
print(font)

count = 0
for glyph_name in font.glyphOrder:
    glyph = font[glyph_name]
    print(glyph)
    print(count)
    if count > 500:
        font.removeGlyph(glyph_name)
    count += 1
    
font.save()