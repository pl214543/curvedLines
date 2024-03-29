# import required libraries
import cv2
import numpy as np

# optimize using Gaussian Blur and Canny Edge
def optimize(frame):

    # Gaussian Blur enabled
    blurred = cv2.GaussianBlur(frame, (5, 5), 0)

    # Canny Edge Detection enabled
    canny = cv2.Canny(blurred, 50, 150, 3)

    # returns the final edited (optimized) variable
    return canny
