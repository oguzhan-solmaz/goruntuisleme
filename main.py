import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.image as mpimg





path = r'C:\indir.jpg'
foto=cv2.imread(path)
cv2.imshow('fotom',foto)
cv2.waitKey(0)


B=foto[:,:,0]
G=foto[:,:,1]
R=foto[:,:,2]




imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray,cmap='gray')
plt.show()




