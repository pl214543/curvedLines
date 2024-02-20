# try cv2.drawContours()

# import required libraries
import cv2
import numpy as num
import math

# import functions
from reader import rectangle, crop
from optimization import optimize
from lineDraw import drawing, contours

# video capture
video = cv2.VideoCapture(0)

print(video.isOpened())

# check if the video is opened

while video.isOpened() == True:
    booleanReady, frame = video.read()

    #print(booleanReady)
    #print(frame)

    height, width = frame.shape[:2]

    zerosRectangle = num.zeros((height, width), dtype="uint8")

    topleftx = int(width * 0.175)
    toplefty = int(height * 0.725)
    bottomrightx = int(width * 0.85)
    bottomrighty = int(height * 0.25)

    varList = [topleftx, toplefty, bottomrightx, bottomrighty]

    # grayscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # uses the functions from the other files to optimize, make a rectangle, and crop
    optimized = optimize(grey)
    rectangled = rectangle(frame, varList)
    cropped = crop(optimized, zerosRectangle, varList)

    # detect the lines
    lines = cv2.HoughLines(cropped, 1, num.pi/180, 200)

    # print(lines)

    contoured = contours(cropped, rectangled)
    # look up how to compare two vectors

    # draw the final lines
    # final = drawing(rectangled, lines)

    # print(final)

    cv2.imshow('Frame', contoured)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
