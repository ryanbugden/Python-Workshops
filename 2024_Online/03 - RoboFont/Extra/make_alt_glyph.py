# menuTitle: Make Alternate Glyph

# Make a functiono that outputs a two-digit number
def format_number(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)


f = CurrentFont()

# Loop through every name in the selected glyph names
for g_name in f.selectedGlyphNames:
    g = f[g_name]
    # Make sure you're getting the non-suffix version of the glyph name
    base_name = g_name.split(".")[0]
    # Do a while loop to figure out the next available stylistic set for this glyph
    i = 1
    new_name = base_name + ".ss0" + format_number(i)
    while new_name in f.keys():
        i += 1
        new_name = base_name + ".ss0" + format_number(i)
    # Copy the glyph (second =) and store it in a new variable (first =)
    new_g = f[new_name] = g
    # Remove any unicode if necessary
    new_g.unicode = None
