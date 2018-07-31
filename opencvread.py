import cv2
import numpy as np 
import  matplotlib.pyplot as plt 
img=cv2.imread('an.jpg',cv2.IMREAD_GRAYSCALE)#grey to save processing power of pc as coloured uses much color
#also to note format of image is chnged to pixel while processing
cv2.imshow('image',img)#takes parametere as what to shw vdeo,image etc and name of object it is stored in
cv2.waitKey(0)#waits for which value image goes out of window ie closes
 #0 here signifies any key can be pressed
cv2.destroyAllWindows()
# """we can do the same using matplotlib in this waitKey"""
# plt.imshow(img,cmap='gray')
# plt.plot([10,200],[50,1000])#this draws one line of give x n y range in matplotlib
# plt.show(
cv2.imwrite("bnw.jpg",img)#this saves the grey img as anothr image in same directory with given name