width = 1590
height = 680
margin = 80

# Make 100 pages
for page_number in range(100):
    # Make the margin bigger each time
    margin += 5
    newPage(width, height)
    fill(random(), random(), random(), 1)
    rect(margin, margin, width-(margin*2), height-(margin*2))
    fill(random(), random(), random(), 1)
    oval(margin, margin, width-(margin*2), height-(margin*2))

saveImage('/Users/Ryan/Documents/Git/public/Python Workshops/2026_Extended/02 - DrawBot/cool_shapes.mp4')