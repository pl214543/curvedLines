# import required libraries
import cv2
import numpy as num

def rectangle(frame):

    # gets height and width of video
    height, width = frame.shape[:2]

    # sets up required parameters for drawing rectangle
    topleftx = width * 0.175
    topleftx = int(topleftx)
    toplefty = height * 0.725
    toplefty = int(toplefty)
    bottomrightx = width * 0.85
    bottomrightx = int(bottomrightx)
    bottomrighty = height * 0.25
    bottomrighty = int(bottomrighty)

    # draws rectangle
    rectangled = cv2.rectangle(frame, (topleftx, toplefty), (bottomrightx, bottomrighty), 255, 3)

    return rectangled

def crop(frame):

    # gets height and width of video
    height, width = frame.shape[:2]

    # sets up required parameters for drawing rectangles
    topleftx = width * 0.175
    topleftx = int(topleftx)
    toplefty = height * 0.725
    toplefty = int(toplefty)
    bottomrightx = width * 0.85
    bottomrightx = int(bottomrightx)
    bottomrighty = height * 0.25
    bottomrighty = int(bottomrighty)

    # creates a mask for cropping out outer edges
    mask = num.zeros(frame.shape[:2], num.uint8)
    mask[toplefty:bottomrighty, topleftx:bottomrightx] = 255

    # crops using the mask
    cropped = cv2.bitwise_and(frame, frame, mask)

    return cropped
