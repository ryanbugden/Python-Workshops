from random import choice

# Set the width and height
w, h = 1000, 1000

# Make a list of three colors, RGB
colors = [
    (1,0,0),
    (0,1,0),
    (0,0,1)
    ]

# Make a blank page, in the specified width and height
newPage(w, h)

# Decide upon a margin to use later
margin = 100
# Make 15 circles
for i in range(15):
    # Set a random color from our list
    # Asterisk formats it without tuple ()s
    fill(*choice(colors))
    # Draw an oval in center with a margin
    oval(margin, margin, w-margin*2, h-margin*2)
    # Increase the margin each time you make a circle
    margin += 30
    
# Save image as a PNG!
saveImage("_output/weird_target.png")
    