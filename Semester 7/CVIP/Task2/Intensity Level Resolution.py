# Intensity Level Resolution
# This relates to the number of intensity levels used to represent image pixel values.
# Reducing the intensity level resolution can be done by reducing the number of bits per pixel.
import cv2
import numpy as np

# Read the image
image = cv2.imread('image1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Reduce intensity resolution to 2 bits
intensity_level_image = np.floor(gray_image / 64) * 64

cv2.imshow('Intensity Level Image', intensity_level_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
