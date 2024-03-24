
for page in range(20):
    newPage()
    center_point = (width()/2, height()/2)
    rotate(3*page, center=center_point)
    scale(page/2, center=center_point)
    skew(-5, center=center_point)
    # Make the line
    stroke(0)
    strokeWidth(50)
    line((10, 10), (990, 990))
    line((990, 10), (10, 990))
    my_radius = 90
    rect(width()/2 - my_radius, height()/2 - my_radius, my_radius*2, my_radius*2)

saveImage("warped_guy.gif")