width = 1000
height = 1000

# Make your own special function for making a styled oval
def make_oval(x, y, w, h):
    stroke(None)
    fill(r=1, g=0, b=0, alpha=1)
    oval(x, y, w, h)

# Make your own special function for making a styled line
def make_line(x1, y1, x2, y2):
    stroke(0.5)
    strokeWidth(10)
    line((x1, y1), (x2, y2))

newPage(width, height)
make_line(100, 100, 900, 900)
make_oval(450, 390, 380, 150)
make_line(100, 688, 590, 900)
make_oval(410, 150, 480, 150)
rect(280, 30, 340, 100)