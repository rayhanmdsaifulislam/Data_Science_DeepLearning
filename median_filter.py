#Importing packages
import cv2 as cv
from skimage.filters import median
from skimage.morphology import disk

#Reading Images
cat_img=cv.imread("cat.jpg")
cow_img=cv.imread("cow.jpg")

#Resize image
cow_img=cv.resize(cow_img, (400, 400))
cat_img=cv.resize(cat_img, (500, 500))

#Apply the median filter [ it use the kernel and disk to add the median value]
img=cv.medianBlur(cow_img, 3)
img1=median(cat_img, disk(3), mode='constant', cval=0.0)

#Showing the image
cv.imshow("Using OpenCV", img)
#cv.imshow("Using Scikit learn", img1)

cv.waitKey(0)
cv.destroyAllWindows()
