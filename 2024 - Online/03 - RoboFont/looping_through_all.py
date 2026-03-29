f = CurrentFont()

# Looping through glyphs
for g in f:
    print(g.name)
    # Break the loop after first glyph
    break
    
print(type(f.layers))
# Looping through layers
for l in f.layers:
    print(l.name)
    # Break the loop after first layer
    break
    
print(type(f.kerning.items()))
# Looping through kerning
for pair, value in f.kerning.items():
    print(pair, value)
    # Break the loop after first pair
    break
    
# Access the features
print(f.features.text)

# Loop through font info
for attr in f.info.fontInfoAttributesVersion3:    
    print(attr)
    try:
        print(getattr(f.info, attr))
    except:
        pass
    
# Get current glyph
g = CurrentGlyph()

# Loop through glyph anchors
for anchor in g.anchors:
    print(anchor)

# Loop through glyph components    
for comp in g.components:
    print(comp)
    
    