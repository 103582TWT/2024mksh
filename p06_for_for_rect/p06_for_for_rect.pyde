# p06_for_for_rect
# 在 600x600裡，放10x10共100格
size(600,600)
background(250,250,0) #背景色
for x in range(10):
    for y in range(10):
        fill(200,250,250) #填充色
        rect(x*60+2.5, y*60+2.5, 55, 55)
