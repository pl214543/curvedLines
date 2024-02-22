# import required libraries
import cv2
import numpy as num

# rectangle function for drawing the rectangle around the mask
def rectangle(frame, varList):

    # draws rectangle on the frame so that the user knows where the mask is
    addRectangle = cv2.rectangle(frame, (varList[0], varList[1]), (varList[2], varList[3]), 255, 3)

    # returns addRectangle variable
    return addRectangle

# crop function for employing the mask so that contours and lines are only detected within a defined space
def crop(frame, zerosRectangle, varList):

    # creates a mask for cropping out outer edges
    mask = cv2.rectangle(zerosRectangle, (varList[0], varList[1]), (varList[2], varList[3]), 255, -1)

    # crops using the mask
    cropped = cv2.bitwise_and(frame, mask)

    # returns the masked image for detection
    return cropped
