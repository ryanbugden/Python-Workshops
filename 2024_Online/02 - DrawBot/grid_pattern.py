from random import random

w, h = 1920, 1080

newPage(w, h)

# Choose some parameters for this grid pattern
margin     = 60
shape_size = 80
density    = 0.5
# Calculate how many rows and columns there should be
rows = int((h - margin*2) / shape_size)
cols = int((w - margin*2) / shape_size)

# Make a custom shape function
def custom_shape(x, y, w, h):
    fill((randint(1, 5)/5), 1, 0.5)
    oval(x, y, w/2, h/2)
    fill((randint(1, 5)/5), 0.3, 1)
    oval(x + w/2, y + h/2, w/2, h/2)

# Backdrop & layout
fill(0)
rect(0, 0, w, h)
# Loop through each row
for row in range(rows):
    # and then loop through each column
    for col in range(cols):
        # Get the X and Y at each position in row/col
        x = margin + col*shape_size
        y = margin + row*shape_size
        # If statement, setting how many gaps there should be
        if random() > density:
            # Run the custom function to draw the shapes!
            custom_shape(x, y, shape_size, shape_size)

# Save a PNG
saveImage("_output/grid_pattern.png")
        