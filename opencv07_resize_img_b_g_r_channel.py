# -*- coding: utf-8 -*-
import cv2
img = cv2.imread("RGB.jpg")
img = cv2.resize(img, (256,256))

cv2.imshow("RGB", img)

# 這裡要把3個channel色層分開
b = img[:,:,0]
g = img[:,:,2]
r = img[:,:,2]

rrr = cv2.merge([r,r,r])
cv2.imshow("RRR", rrr)
bbb = cv2.merge([b,b,b])
cv2.imshow("BBB", bbb)
ggg = cv2.merge([g,g,g])
cv2.imshow("GGG", ggg)

cv2.waitKey(0)
cv2.destroyAllWindows()