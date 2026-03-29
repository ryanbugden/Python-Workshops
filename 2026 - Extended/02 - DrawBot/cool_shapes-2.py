width = 1590
height = 680
margin = 80

# Make 100 pages
for page_number in range(100):
    # Make the margin bigger by 5 each page
    margin += 5
    # Make a new page
    newPage(width, height)
    # Set a random fill color for a rectangle
    fill(random(), random(), random(), 1)
    # Make a rectangle that fits the space, up to the margin
    rect(margin, margin, width-(margin*2), height-(margin*2))
    # Set a random fill color for an oval
    fill(random(), random(), random(), 1)
    # Make an oval that fits the space, up to the margin
    oval(margin, margin, width-(margin*2), height-(margin*2))

saveImage('cool_shapes.mp4')