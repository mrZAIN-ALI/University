# Spatial Resolution
# Spatial resolution refers to the amount of detail in an image and can be altered by resizing the image.

import cv2

# Read the image
image = cv2.imread('image.jpg')

# Reduce the resolution
low_res_image = cv2.resize(image, (100, 100))

# Increase the resolution
high_res_image = cv2.resize(image, (800, 800))

# Show the images
cv2.imshow('Low Resolution Image', low_res_image)
cv2.imshow('High Resolution Image', high_res_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
