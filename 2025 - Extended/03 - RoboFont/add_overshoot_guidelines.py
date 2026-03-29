# Choose the overshoot value
overshoot = 10
# Choose the name you want for all of your overshoots
guideline_name = "overshoot"

font = CurrentFont()

# Clear guidelines first
for guideline in font.guidelines:
    if guideline.name == guideline_name:
        font.removeGuideline(guideline)

# Add new ones
below = [font.info.descender, 0]
above = [font.info.xHeight, font.info.capHeight, font.info.ascender]

# Loop through every font dimension below which you'd like an overshoot guideline
for y in below:
    font.appendGuideline(
        # Add it below that y
        position=(0, y - overshoot), 
        angle=0, 
        name=guideline_name, 
        )
        
# Loop through every font dimension above which you'd like an overshoot guideline
for y in above:
    font.appendGuideline(
        # Add it above that y
        position=(0, y + overshoot), 
        angle=0, 
        name=guideline_name, 
        )