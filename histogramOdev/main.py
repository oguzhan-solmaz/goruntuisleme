import cv2
import numpy as np




def write(histogram):
    for k in range (0,256):
        print(k,"=",histogram[k])

path=cv2.imread("C:\indir.jpg",0)


histogram= np.zeros(256)
[h,w]=np.shape(path)
for i in range (0,h):
    for j in range (0,w):
        k=path[i,j]
        histogram[k]=histogram[k]+1

write(histogram)
cv2.imshow("grey foto",path)
cv2.waitKey()



