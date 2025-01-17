# Image Enhancement
# Image enhancement can involve a variety of techniques, including histogram equalization for contrast improvement.

import cv2

# Read the image
image = cv2.imread('image1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY )

# Histogram equalization to enhance contrast
enhanced_image = cv2.equalizeHist(gray_image)

cv2.imshow('Enhanced Image', enhanced_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
