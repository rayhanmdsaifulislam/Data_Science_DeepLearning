#Importing packages
import bm3d
import cv2 as cv
import numpy as np
from skimage import io, img_as_float

#Read a Image
img=img_as_float((io.imread("cat.jpg", as_gray=False)))

#Resize Image
img=cv.resize(img, (300, 300))

#Apply BM3D filter
BM3D_denoised_image=bm3d.bm3d(img, sigma_psd=0.3)

#Display the Image
cv.imshow("Image",BM3D_denoised_image)
cv.waitKey(0)
cv.destroyAllWindows()