font = CurrentFont()

# Loop through all possible font info attributes
for attribute in font.info.fontInfoAttributesVersion3:
    # Ignore this one which might raise an error
    if attribute == "guidelines":
        continue
    # Print this current font’s info
    print(attribute, getattr(font.info, attribute))