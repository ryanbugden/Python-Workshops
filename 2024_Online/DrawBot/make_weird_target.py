# Set the width and height
w, h = 1000, 1000
# Decide upon a margin to use later
margin = 100

# Make a blank page, in the specified width and height
newPage(w, h)

# Make 15 circles
for i in range(15):
    # Set a random RGB color
    fill(random(), random(), random())
    oval(margin, margin, w-margin*2, h-margin*2)
    # Increase the margin each time you make a circle
    margin += 30
    