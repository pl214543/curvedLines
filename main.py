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

    # grayscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # uses the functions from the other files to optimize, make a rectangle, and crop
    optimized = optimize(grey)
    rectangled = rectangle(frame)
    cropped = crop(optimized)

    # detect the lines
    lines = cv2.HoughLines(cropped, 1, num.pi/180, 200)

    # print(lines)

    contoured = contours(optimized, rectangled)
    # look up how to compare two vectors

    # draw the final lines
    # final = drawing(rectangled, lines)

    # print(final)

    cv2.imshow('Frame', contoured)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
