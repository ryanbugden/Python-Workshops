width = 1590
height = 680
margin = 80
# Manually choose 3 of my favorite colors
my_colors = [
    (1, 0, 0, 1),
    (0, 1, 0, 1),
    (0, 0, 1, 1),
]

# Make 100 pages
for page_number in range(100):
    # Increase the margin each time
    margin += 5
    newPage(width, height)
    # Randomly set the first color and make a rect
    fill(*choice(my_colors))
    rect(margin, margin, width-(margin*2), height-(margin*2))
    # Randomly set the second color and make an oval
    fill(*choice(my_colors))
    oval(margin, margin, width-(margin*2), height-(margin*2))

# Save a video comprised of all of the pages made above
saveImage('/Users/Ryan/Documents/Git/public/Python Workshops/2026_Extended/02 - DrawBot/cool_shapes.mp4')