# menuTitle: Jostle My Glyphs

from random import randint


jostle_amount = 20

f = CurrentFont()

for g in f:
    mid_y = (g.bounds[3] + g.bounds[1]) / 2
    g.rotateBy(randint(-jostle_amount, jostle_amount), origin=(g.width, mid_y))
    