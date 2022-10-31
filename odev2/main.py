import cv2
import numpy as np

foto=cv2.imread("C:\indir.jpg",0)
cv2.imshow("cicek",foto)
cv2.waitKey()

max=np.max(foto)

[x,y]=np.shape(foto)

for k in range (0,x):
    #matrisden max görüntü yoğunluğunu çıkarıyoruz
    for l in range (0,y):
        foto[k,l]=max-foto[k,l]

cv2.imshow("terscicek",foto)
cv2.waitKey()



