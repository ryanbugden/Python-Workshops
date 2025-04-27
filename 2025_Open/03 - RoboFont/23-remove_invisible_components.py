# menuTitle: Remove Invisible Components


# ————— SUBJECTIVE —————

# Decide if you just want to check for issues, or actually remove components
actually_remove = True


# ————— OBJECTIVE —————

# Get the font object
font = CurrentFont()
# Loop through every glyph in the font
for glyph in font:
    # Loop through every component in the glyph
    for component in glyph.components:
        # Check to see if the component’s base glyph is even in the font
        if component.baseGlyph not in font.keys():
            # If not, remove the component
            if actually_remove:
                print(f"{component.baseGlyph} is not in the font!. Removing {component.baseGlyph} from {glyph.name}.")
                glyph.removeComponent(component)
            else:
                print(f"{component.baseGlyph} is not in the font!")

print("✅ Done scanning!")
            
            