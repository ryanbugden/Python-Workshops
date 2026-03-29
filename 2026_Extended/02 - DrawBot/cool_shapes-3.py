width = 1590
height = 680
margin = 80
# Randomize 1 palette to use for the whole script
my_colors = [
    (random(), random(), random(), 1),
    (random(), random(), random(), 1),
    (random(), random(), random(), 1),
]

for page_number in range(100):
    color_1 = choice(my_colors)
    color_2 = choice(my_colors)
    # Make sure the colors aren't the same
    if color_2 == color_1:
        position = my_colors.index(color_2)
        # If so, get the previous color in the list
        color_2 = my_colors[position-1]
    
    # Make the margin bigger each page!
    margin += 5
    newPage(width, height)
    
    # Set the stroke width to a random integer between 10 and 100
    strokeWidth(randint(10, 100))
    fill(*color_1)
    stroke(*color_2)
    rect(margin, margin, width-(margin*2), height-(margin*2))
    
    fill(*color_2)
    stroke(0)
    oval(margin, margin, width-(margin*2), height-(margin*2))

saveImage('/Users/Ryan/Documents/Git/public/Python Workshops/2026_Extended/02 - DrawBot/cool_shapes-other_random.mp4')