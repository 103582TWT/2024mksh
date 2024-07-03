# p11_for_many_image
def setup():
    global imgBG, imgSun
    size(625,400) #用你的background.jpg圖的大小
    imgBG = loadImage("background.jpg")
    imgSun = loadImage("sun.png") #找半透明的png圖
def draw():
    global imgBG, imgSun
    image(imgBG, 0, 0)
    for i in range(10):
        image(imgSun, i*100, 0, 300, 300)
    image(imgSun, mouseX-150, mouseY-150, 300,300)
