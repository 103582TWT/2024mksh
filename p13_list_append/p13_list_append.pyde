# p13_list_append
def setup():
    global imgBG, imgSun
    size(625,400) #用你的background.jpg圖的大小
    imgBG = loadImage("background.jpg")
    imgSun = loadImage("sun.png") #找半透明的png圖
def draw():
    global imgBG, imgSun
    image(imgBG, 0, 0)
    for i in range(len(x)):
        image(imgSun, x[i]-150, y[i]-150, 300, 300)
    image(imgSun, mouseX-150, mouseY-150, 300,300)
x = [] # x = [0]*10
y = [] # y = [0]*10
#N = 0
def mousePressed():
    x.append(mouseX) #global N
    y.append(mouseY) #x[N], y[N] = mouseX, mouseY
    #N+=1
