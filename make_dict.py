import numpy as np
import cv2
import cv2.aruco as aruco
 
 
'''
    drawMarker(...)
        drawMarker(dictionary, id, sidePixels[, img[, borderBits]]) -> img
'''
 
aruco_dict = aruco.Dictionary_get(aruco.DICT_3X3_100)
print(aruco_dict)
# second parameter is id number
# last parameter is total image size
img = aruco.drawMarker(aruco_dict, 2, 500)
cv2.imwrite("test_marker.jpg", img)
 
cv2.imshow('frame',img)

key = cv2.waitKey(1000)

cv2.destroyAllWindows()

