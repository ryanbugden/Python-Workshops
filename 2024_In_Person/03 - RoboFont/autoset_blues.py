# menuTitle: Auto-Set Blue Zones

font = CurrentFont()

# Choose letters to inform the blue zones
baseline_zone = ('a', 'b', 'c', 'd', 'e', 's', 't', 'u', 'o', 'O', 'V')  #etc.
xheight_zone  = ('a', 'c', 'e', 'm', 'n', 'o', 'p', 'q', 'r', 's')  # etc.
cap_zone      = ('A', 'B', 'C', 'D', 'E', 'F', 'G')  # etc.
asc_zone      = ('b', 'd', 'l', 'k', 'h', 'f')  # etc.
desc_zone     = ('p', 'q', 'g', 'y')  #etc

# Make a function that gives you the lowest and highest point in the glyph
def get_min_max(font, list_of_glyphs):
    # Make empty lists you're about to fill
    all_mins = []
    all_maxs = []
    for glyph_name in list_of_glyphs:
        glyph = font[glyph_name]
        glyph_y_min, glyph_y_max = glyph.bounds[1], glyph.bounds[3]
        all_mins.append(glyph_y_min)
        all_maxs.append(glyph_y_max)
    # Get the lowest low and the highest high
    y_min = min(all_mins)
    y_max = max(all_maxs)
    # Output these values from the function
    return y_min, y_max

# Get the baseline zone
baseline_y_min, baseline_y_max = get_min_max(font, baseline_zone)
baseline_list = [baseline_y_min, 0]
# Get the x-height zone
xheight_y_min, xheight_y_max = get_min_max(font, xheight_zone)
xheight_list = [font.info.xHeight, xheight_y_max]
# Get the cap-height zone
cap_y_min, cap_y_max = get_min_max(font, cap_zone)
cap_list = [font.info.capHeight, cap_y_max]
# Get the ascenders zone
asc_y_min, asc_y_max = get_min_max(font, asc_zone)
asc_list = [font.info.ascender, asc_y_max]
# Get the descender zone
desc_y_min, desc_y_max = get_min_max(font, desc_zone)
desc_list = [desc_y_min, font.info.descender]

# Set the main blue values
font.info.postscriptBlueValues = baseline_list + xheight_list + cap_list + asc_list
# Put the descender zone in the "other-blues"
font.info.postscriptOtherBlues = desc_list



