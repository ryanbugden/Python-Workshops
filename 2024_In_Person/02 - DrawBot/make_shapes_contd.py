from random import random

my_width = 1920    
my_height = 1080
newPage(my_width, my_height)
fill(r=1, g=0, b=0, alpha=1)
rect(0, 0, my_width, my_height)

my_radius = 500
for number in range(10):
    print("Drawing an oval")
    fill(random(), random(), random())
    oval(my_width/2 - my_radius, my_height/2 - my_radius, my_radius*2, my_radius*2)
    my_radius -= 50

