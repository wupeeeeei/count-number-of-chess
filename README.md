# count-number-of-chess
計算出所附圖像(共三張)每張圖像中圍棋個數

操作環境
Windows 10
pychram
OpenCV 4.5.2
Python 3.6
 
程式說明
1. 把圖片轉成灰階
2. 把圖片二值化
3. 用erode()和dilate()處理旗子
4. 用findContours()處理旗子輪廓
5. 用drawContours()於畫出輪廓
6. 印出數量

測試圖片:
![image](https://github.com/wupeeeeei/count-number-of-chess/blob/main/IMG_5702.JPG)
![image](https://github.com/wupeeeeei/count-number-of-chess/blob/main/IMG_5703.JPG)
![image](https://github.com/wupeeeeei/count-number-of-chess/blob/main/IMG_5704.JPG)
