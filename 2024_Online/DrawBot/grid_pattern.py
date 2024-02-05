from random import random

w, h = 1920, 1080

newPage(w, h)

margin     = 60
shape_size = 80
density    = 0.5
rows = int((h - margin*2) / shape_size)
cols = int((w - margin*2) / shape_size)

# Make a custom shape
def custom_shape(x, y, w, h):
    fill((randint(1, 5)/5), 1, 0.5)
    oval(x, y, w/2, h/2)
    fill((randint(1, 5)/5), 0.3, 1)
    oval(x + w/2, y + h/2, w/2, h/2)

# Backdrop & layout
fill(0)
rect(0, 0, w, h)
for row in range(rows):
    for col in range(cols):
        x = margin + col*shape_size
        y = margin + row*shape_size
        if random() > density:
            custom_shape(x, y, shape_size, shape_size)

saveImage("~/Desktop/grid_pattern.png")
        