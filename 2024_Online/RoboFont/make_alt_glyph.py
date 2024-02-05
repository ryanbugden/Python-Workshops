# menuTitle: Make Alternate Glyph


def format_number(number):
    if number < 10:
        return "0" + str(number)
    else:
        return str(number)


f = CurrentFont()

for g_name in f.selectedGlyphNames:
    g = f[g_name]
    base_name = g_name.split(".")[0]
    
    i = 1
    new_name = base_name + ".ss0" + format_number(i)
    while new_name in f.keys():
        i += 1
        new_name = base_name + ".ss0" + format_number(i)
    
    new_g = f[new_name] = g
    new_g.unicode = None
