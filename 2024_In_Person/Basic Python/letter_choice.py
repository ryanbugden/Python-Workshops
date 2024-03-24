lowercase_glyphs = ["a", "b", "c"]
uppercase_glyphs = []
for glyph in lowercase_glyphs:
    uppercase_glyphs += [glyph.upper()]
    
print(uppercase_glyphs)



letters = "wertyui?"
print(choice(letters))