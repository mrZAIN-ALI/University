# Bit Plane Slicing
# Bit plane slicing extracts specific bits from the pixel values to highlight certain features.

import cv2
import numpy as np

# Read the image
image = cv2.imread('map.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extract the bit plane for map image
bit_plane = np.bitwise_and(gray_image, 2**7)

cv2.imshow('Bit Plane 7 Image', bit_plane)
cv2.waitKey(0)
cv2.destroyAllWindows()
