# Log Transformation
# Log transformation helps to expand the dark pixels of an image.
import cv2
import numpy as np

# Read the image
image = cv2.imread('image1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply log transformation
c = 255 / np.log(1 + np.max(gray_image))
log_transformed = c * (np.log(1 + gray_image))

# Convert to uint8
log_transformed = np.array(log_transformed, dtype=np.uint8)

cv2.imshow('Log Transformed Image', log_transformed)
cv2.waitKey(0)
cv2.destroyAllWindows()
