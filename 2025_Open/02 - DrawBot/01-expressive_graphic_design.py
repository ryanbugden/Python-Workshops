# Make variables representing the desired width and height of the canvas
width = 2000
height = 2000

# Make a new canvas with that width and height
newPage(width, height)

# Make a random rectangle (defaults to black fill, no stroke)
rect(600, 400, 125, 460)

# Fill the upcoming shape with red
fill(1,0,0)

# Make an oval
oval(30, 50, 300, 660)

# Stroke the upcoming shape red, with a 50 stroke thickness
stroke(1,0,0)
strokeWidth(50)

# Draw a line
line((40, 30), (990, 1240))