t = 200
def setup():
    size(500,400)
def draw():
    background(0)
    stroke(92,0,0)
    strokeWeight(6)
    noFill()
    global t
    cSize = t
    t -= 5
    if t==0: t = 200
    ellipse(250,200,cSize,cSize)
    fill(193,33,33)
    ellipse(250,200,40,40)
