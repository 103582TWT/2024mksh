def setup():
    size(400,400)
def draw():
    background(230,216,221)
    stroke(205,216,221)
    for x in range(0,400,50):
        line(x, x, x, 400)
    for y in range(0,400,50):
        line(0, y, 400, y)
