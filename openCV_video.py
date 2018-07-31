import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('save.avi',fourcc,20.0,(640,480))
while True:
	ret,frame=cap.read()
	x=0;y=0
	w=200;h=300

	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	
	cv2.line(frame,(100,100),(300,400),(0,0,0),20)
	cv2.putText(frame, 'How are you', (100,100), cv2.FONT_HERSHEY_PLAIN,10,(0,255,0),5)
	cv2.ellipse(frame, (250, 150), (80, 20), 5, 0, 360,(0,0,255))
	cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),-1)
	cv2.circle(frame,(100,100),90,(0,0,0),5)
	cv2.imshow('frame title',frame)
	#cv2.imshow('gray title',gray)
	out.write(frame)
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break
cap.release()
out.release()
cv2.destroyAllWindows()		
#sphinx library for audio recording
#cascade classifier
#detect multiscale
