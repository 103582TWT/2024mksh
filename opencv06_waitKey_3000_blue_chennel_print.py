# -*- coding: utf-8 -*-
import cv2
# 要先把圖檔放到同一個目錄(桌面)
# 小心附檔名 檔案總管 檢視 勾副檔名
img = cv2.imread("mksh.png")
b = img[:,:,0] # 藍色的channel
print(b)

cv2.imshow("opencv06", img)
cv2.waitKey(3000) # 等按空白鍵
# 等三秒鐘都沒按鍵就關閉視窗
cv2.destroyAllWindows() # 再關視窗