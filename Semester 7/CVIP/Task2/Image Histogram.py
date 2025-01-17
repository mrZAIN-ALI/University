# Image Histogram
# The histogram of an image shows the distribution of intensities. It can be computed and plotted using OpenCV.
import matplotlib.pyplot as plt
import cv2

# Read the image
image = cv2.imread('image1.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Compute the histogram
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot the histogram
plt.plot(histogram)
plt.title('Histogram')
plt.show()
