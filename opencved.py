import cv2
import numpy as np 
cap=cv2.VideoCapture(0)#reads cam and signifies frts cam or sec or third camera
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('codevid.avi',fourcc,20.0,(640,480))

while True:
	ret,frame=cap.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

	cv2.imshow('THIS IS FRAME TITLE',frame)#opens two screen used to compare
	cv2.imshow('THIS IS gray TITLE',gray)#gray vdeo screen
	out.write(frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()

