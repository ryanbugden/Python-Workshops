font = CurrentFont()

# Remove empty groups from font 
for group_name, members in font.groups.items():
    if len(members) == 0:
        print(f"Removing {group_name} from font.")
        font.groups.pop(group_name)

for pair, value in font.kerning.items():
    left, right = pair
    # Get all the pairs that have only groups involved.
    if left in font.groups.keys() and right in font.groups.keys():
        print(pair)
        
# Find which group each glyph is in
print(font.groups.findGlyph("a"))
print(font.groups.findGlyph("n"))

# Store all pairs where this group is in the left side of the pair
left_pairs = []
for pair, value in font.kerning.items():
    left, right = pair
    if left == 'public.kern1.LAT_a':
        left_pairs.append(pair)
        
# Set a specific kerning pair’s value (try doing this to many in a loop)
print(font.kerning[('public.kern1.LAT_a', 'V')])
font.kerning[('public.kern1.LAT_a', 'V')] = 50
print(font.kerning[('public.kern1.LAT_a', 'V')])

