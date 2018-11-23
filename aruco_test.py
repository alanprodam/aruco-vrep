import numpy as np
import cv2
import cv2.aruco as aruco
import sys, time, math

#-- Define Tag
id_to_find = 72
merer_size = 10 #-cm

#-- 180 deg rotation matrix around x axis
R_flip = np.zeros((3,3), dtype=np.float)
R_flip[0,0] = 1.0
R_flip[1,1] = -1.0
R_flip[2,2] = -1.0

#-- Define the aruco dictionary
aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_6X6_250)
parameters = aruco.DetectorParameters_create()

#-- Capture the videocamera (this may also be a video or picture)
#-- Create an object. One for External Camera/ Zero for Internal Camera
cap = cv2.VideoCapture(1)
#-- Set the camera size as the one it was calibration with
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while(True):
	
	#-- Create and read a frame object
	check, frame = cap.read()
	#print(check)
	#print(frame)
	
	#-- Convert in gray scale
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #-- remember, Opencv stores color images in Blue, Green, Red
	
	#-- Find all the aruco markers in the images
	corners, ids, rejected = aruco.detectMarkers(image=frame, dictionary=aruco_dict, parameters=parameters)
	
	frame = aruco.drawDetectedMarkers(frame, corners)
	
	#-- Show de frame
	cv2.imshow("Frame",frame)

	key = cv2.waitKey(1)
	if key == ord('q'):
		break
		
# When everything done, release the capture
cap.release()
#cv2.destroyAllWindows()