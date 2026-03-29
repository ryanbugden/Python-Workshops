f = CurrentFont()

# Make a function that makes glyphs of multiple components of other glyphs
def make_logotype(string):
    '''Note: Currently only support glyphs whose names are equal to how they’re typed.'''
    new_glyph = f.newGlyph(string, clear=True)
    cursor = 0
    for letter in string:
        new_glyph.appendComponent(letter, offset=(cursor, 0))
        cursor += f[letter].width
    # Set the right sidebearing of the wordmark equal to that of the last glyph
    new_glyph.rightMargin = f[letter].rightMargin

# Make one for "Python"
word = "Python"
make_logotype(word)