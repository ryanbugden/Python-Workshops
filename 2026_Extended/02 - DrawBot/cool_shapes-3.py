width = 1920
height = 1080
margin = 80

# Randomize 1 palette to use for the whole script
my_colors = [
    (random(), random(), random(), 1),
    (random(), random(), random(), 1),
    (random(), random(), random(), 1),
]

# Loop through 100 numbers
for page_number in range(100):
    # Each time, randomly choose two colors from my list above and store them in variables
    color_1 = choice(my_colors)
    color_2 = choice(my_colors)
    # If the colors are the same...
    if color_2 == color_1:
        position = my_colors.index(color_2)
        # ... get the previous color in the list
        color_2 = my_colors[position-1]
    
    # Make the margin bigger each page!
    margin += 5
    newPage(width, height)
    
    # Set the stroke width to a random integer between 10 and 100
    strokeWidth(randint(10, 100))
    # We need to unpack the 1 tuple into 4 separate arguments with "*"
    fill(*color_1)
    stroke(*color_2)
    rect(margin, margin, width-(margin*2), height-(margin*2))
    
    fill(*color_2)
    stroke(0)
    oval(margin, margin, width-(margin*2), height-(margin*2))

saveImage('cool_shapes-other_random.mp4')