# menuTitle: Auto-Set Blue Zones


font = CurrentFont()

baseline_zone = ('o', 'v', 'a', "O", "b", "c", "d", "e", "s", "t", "u")  #etc.
xheight_zone  = ('a', 'c', 'e', 'm', 'n', 'o', 'p', 'q', 'r', 's')  # etc.
cap_zone      = ('A', 'B', 'C', 'D', 'E', 'F', 'G')  # etc.
asc_zone      = ('b', 'd', 'l', 'k', 'h', 'f')  # etc.
desc_zone     = ('p', 'q', 'g', 'y')  #etc

def get_min_max(font, list_of_glyphs):
    all_mins = []
    all_maxs = []
    for glyph_name in list_of_glyphs:
        glyph = font[glyph_name]
        glyph_y_min, glyph_y_max = glyph.bounds[1], glyph.bounds[3]
        all_mins.append(glyph_y_min)
        all_maxs.append(glyph_y_max)
    y_min = min(all_mins)
    y_max = max(all_maxs)

    return y_min, y_max


baseline_y_min, baseline_y_max =get_min_max(font, baseline_zone)
baseline_list = [baseline_y_min, 0]

xheight_y_min, xheight_y_max = get_min_max(font, xheight_zone)
xheight_list = [font.info.xHeight, xheight_y_max]

cap_y_min, cap_y_max = get_min_max(font, cap_zone)
cap_list = [font.info.capHeight, cap_y_max]

asc_y_min, asc_y_max = get_min_max(font, asc_zone)
asc_list = [font.info.ascender, asc_y_max]

desc_y_min, desc_y_max = get_min_max(font, desc_zone)
desc_list = [desc_y_min, font.info.descender]

font.info.postscriptBlueValues = baseline_list + xheight_list + cap_list + asc_list
font.info.postscriptOtherBlues = desc_list



