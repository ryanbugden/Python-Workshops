# Loop through 20 pages
for page_number in range(20):
    # Make a page
    newPage()
    # Get the center point of the page
    center_point = (width()/2, height()/2)
    # Rotate, more for each page
    rotate(3 * page_number, center=center_point)
    scale(page_number / 2, center=center_point)
    skew(-5, center=center_point)
    # Make the art
    # Draw the line
    stroke(0)
    strokeWidth(50)
    line((10, 10), (990, 990))
    line((990, 10), (10, 990))
    # Draw a rect, using a radius for some reason
    my_radius = 90
    rect(width()/2 - my_radius, height()/2 - my_radius, my_radius*2, my_radius*2)

# Save all pages into 1 GIF
saveImage("_output/warped_guy.gif")