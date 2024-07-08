# -*- coding: utf-8 -*-

import cv2 # 使用 OpenCV 的 cv2 外掛
# 匯入cv2
img = cv2.imread("onepiece.jpg")
# 讀入 opencv.jpg 這張圖，小心附檔名
cv2.imshow("opencv01", img) # 要在'opencv01'秀圖
cv2.imshow("opencv02", img) # 要在'opencv02'秀圖
cv2.imshow("opencv03", img) # 要在'opencv03'秀圖
cv2.waitKey(0) #等待任意鍵，卡住，不要結束
# File-New Ctrl-N 開新檔案
# File-Save as 另存新檔 opencv01.py
# 「桌面」
# 先寫好，不要執行，不然會當機
# 圖也要放在同一個目錄「桌面」