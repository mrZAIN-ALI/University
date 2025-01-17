# Read Image Copy Image and Move the Image
import cv2
import os
import time

# Read image
img = cv2.imread('image.png')

# Display image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Copy image
copy = img.copy()
# Save image
cv2.imwrite('copy.png', copy)

# Move image to folder
os.rename('copy.png', './image/image.png')
