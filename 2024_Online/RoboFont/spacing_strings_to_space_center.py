# menuTitle: Spacing Strings to Space Center

from mojo.UI import CurrentSpaceCenter

f = CurrentFont()

text = ''
for g_name in f.selectedGlyphNames:
    g = f[g_name]
    text += f"HH/{g.name} HH OO/{g.name} OO\\n"
    
CurrentSpaceCenter().setRaw(text)

