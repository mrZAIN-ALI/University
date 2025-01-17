# Power Law (Gamma) Transformation
# Power law transformation (Gamma correction) controls the brightness of an image.

import cv2
import numpy as np

# Read the image
image = cv2.imread('image1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gamma = 2.0 # Example gamma value
gamma_transformed = np.array(255 * (gray_image / 255) ** gamma, dtype='uint8')

cv2.imshow('Gamma Transformed Image', gamma_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
