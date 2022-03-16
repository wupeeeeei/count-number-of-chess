import cv2
import numpy as np
img = cv2.imread('IMG_5704.JPG', 0)
cv2.namedWindow('Input', cv2.WINDOW_NORMAL)
cv2.imshow('Input', img)
ret,out1 = cv2.threshold(img, 127, 255,cv2.THRESH_BINARY_INV)
cv2.namedWindow('Binay', cv2.WINDOW_NORMAL)
cv2.imshow('Binay', out1)
kernel1= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(200,200))#300,200,200
erosion = cv2.erode(out1, kernel1)
cv2.namedWindow('erode', cv2.WINDOW_NORMAL)
cv2.imshow('erode', erosion)
kernel2= cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(50,50))#80,50,50
dilation = cv2.dilate(erosion, kernel2)
cv2.namedWindow('dilate', cv2.WINDOW_NORMAL)
cv2.imshow('dilate', dilation)
contours, hierarchy = cv2.findContours(dilation,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.imread('IMG_5704.JPG')
cv2.drawContours(img,contours,-1,(0,255,0),20)
cv2.namedWindow('Result', cv2.WINDOW_NORMAL)
cv2.imshow('Result', img)
print(str(len(contours)))
cv2.waitKey(0)