#Importing packages
import cv2 as cv

#Read a Image
img=cv.imread("cow.jpg", 1)

#Resize Image
img=cv.resize(img, (320, 240))
img_org=img

#Apply the Bilateral filter
bi_img=cv.bilateralFilter(img, 10, 15, 15, borderType=cv.BORDER_DEFAULT)

#Apply the Median Filter
med_img=cv.medianBlur(img, 5)

#Apply the Gaussian filter
#gau_img=cv.GaussianBlur(img, 5, borderType=cv.BORDER_DEFAULT)

#Showing the image
cv.imshow("Filtered Image", bi_img)
cv.imshow("Original Image", img_org)
cv.imshow("Median Filter", med_img)
#cv.imshow("Gaussian filter", gau_img)
cv.waitKey(0)
cv.destroyAllWindows()