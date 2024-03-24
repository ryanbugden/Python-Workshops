my_width = 1920    
my_height = 1080
newPage(my_width, my_height)
fill(r=1, g=0, b=0, alpha=1)
rect(0, 0, my_width, my_height)
fill(0, 0, 1)

my_radius = 500
oval(my_width/2 - my_radius, my_height/2 - my_radius, my_radius*2, my_radius*2)
saveImage('my_shapes.pdf')