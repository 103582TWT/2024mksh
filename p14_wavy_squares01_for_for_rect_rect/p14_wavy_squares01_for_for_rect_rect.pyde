# p14_wavy_squares01_for_for_rect_rect
size(480,480)
background(0, 0, 0)
for x in range(16):
    for y in range(16):
        rect(x*30, y*30,30,30)
        rect(x*30+2, y*30+2,9,9)
        rect(x*30+19, y*30+19,9,9)
        
