# import required libraries
import cv2
import numpy as num

def rectangle(frame, varList):

    # draws rectangle
    rectangled = cv2.rectangle(frame, (varList[0], varList[1]), (varList[2], varList[3]), 255, 3)

    return rectangled

def crop(frame, zerosRectangle, varList):

    # creates a mask for cropping out outer edges
    mask = cv2.rectangle(zerosRectangle, (varList[0], varList[1]), (varList[2], varList[3]), 255, -1)

    # crops using the mask
    cropped = cv2.bitwise_and(frame, mask)

    return cropped
