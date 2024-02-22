# LINES NOTATED

# import required libraries
import cv2
import numpy as num

# import functions
from reader import rectangle, crop
from optimization import optimize
from lineDraw import drawing, contours

# video capture
video = cv2.VideoCapture(0)

# test case
print(video.isOpened())

# check if the video is opened
while video.isOpened():

    # gets the frame from the video to draw on
    booleanReady, frame = video.read()

    # retrieves the height and width of the frame for masking
    height, width = frame.shape[:2]

    # creates a rectangle with background of 0s for masking
    zerosRectangle = num.zeros((height, width), dtype="uint8")

    # defines coordinates for masking as percentage of camera view so compatible with any camera
    topLeftX = int(width * 0.175)
    topLeftY = int(height * 0.725)
    bottomRightX = int(width * 0.85)
    bottomRightY = int(height * 0.25)

    # creates list of those coordinates for drawing the rectangles and masking later, easy to use as parameters
    varList = [topLeftX, topLeftY, bottomRightX, bottomRightY]

    # grayscale
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # uses the functions from the other files to optimize, make a rectangle, and crop
    # optimize will employ Gaussian Blur and Canny Edge Detection
    optimized = optimize(grey)

    # cropped will create the mask
    cropped = crop(optimized, zerosRectangle, varList)

    # detect the lines using HoughLines
    lines = cv2.HoughLines(cropped, 1, num.pi/180, 200)
    # linesP = cv2.HoughLinesP(cropped, 1, num.pi/180, 200, 5, 5)

    # calls the contours function to detect contours and draw
    contoured = contours(cropped, frame)

    # look up how to compare two vectors

    # draw the final lines
    # final = drawing(addRectangle, lines)

    # final = probablistic(addRectangle, linesP)

    # addRectangle will draw the rectangle around the mask. put after others so contours doesn't detect the rectangle
    addRectangle = rectangle(contoured, varList)

    # display the frame, creating a video
    cv2.imshow('Frame', addRectangle)

    # closes the window when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# releases the video capture
video.release()

# closes the video
cv2.destroyAllWindows()
