# Make a new list that is an uppercase version of the first list
lowercase_glyphs = ["a", "b", "c"]
uppercase_glyphs = []
for glyph in lowercase_glyphs:
    uppercase_glyphs += [glyph.upper()]    
print(uppercase_glyphs)

# Make a string, and choose a letter from the string
letters = "wertyui?"
print(choice(letters))