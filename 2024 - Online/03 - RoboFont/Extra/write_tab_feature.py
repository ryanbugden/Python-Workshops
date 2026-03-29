# menuTitle: Write Tabular Figures Feature

f = CurrentFont()

# Start off the feature code
tab_feature = """
feature tnum {
    sub @default_figures by @tabular_figures;
} tnum;
"""

# Make lists of glyph names to fill in the @ definitions
tab_on  = []
tab_off = []
for g_name in f.glyphOrder:
    if '.tnum' in g_name:
        tab_on.append(g_name)
        tab_off.append(g_name.replace(".tnum", "     "))

tab_on  = f"@tabular_figures = [{' '.join(tab_on)}];\n"
tab_off = f"@default_figures = [{' '.join(tab_off)}];\n"

# Inject the features into the font
f.features.text = tab_on + tab_off + tab_feature
