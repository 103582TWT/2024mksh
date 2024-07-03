# p08_two_image
size(625,400) #用你的background.jpg圖的大小
imgBG = loadImage("background.jpg")
image(imgBG, 0, 0)
imgSun = loadImage("sun.png") #找半透明的png圖
image(imgSun, 50, 50, 300,300)
