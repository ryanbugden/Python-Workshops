f = CurrentFont()

caps = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
lc   = ('a', 'c', 'e', 'g', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z')
asc  = ('b', 'd', 'f', 'h', 'l')
desc = ('g', 'j', 'y', 'p', 'q')
base = ('C', 'G', 'O', 'S', 'U', 'a', 'b', 'c', 'd', 'e', 'o', 's', 'u')

def get_min_max(glyph_names):
    minimum = 0
    maximum = 0
    for g_name in glyph_names:
        print(g_name)
        g = f[g_name]
        if g.bounds[1] < minimum:
            minimum = g.bounds[1]
        if g.bounds[3] > maximum:
            maximum = g.bounds[3]
    return minimum, maximum

cap_min, cap_max = get_min_max(caps)
x_min, x_max     = get_min_max(lc)
asc_min, asc_max = get_min_max(asc)
base_min, _      = get_min_max(base)
desc_min, _      = get_min_max(desc)

f.info.postscriptBlueValues = [
                                base_min, 0, 
                                f["x"].bounds[3], x_max, 
                                f["H"].bounds[3], cap_max, 
                                f["b"].bounds[3], asc_max
                              ]
                              
f.info.postscriptOtherBlues = [desc_min, f["p"].bounds[1]]