# import required libraries
import cv2
import numpy as num

count = 0

# function for drawing the straight lines
def drawing(frame, lines):

    # checks if anything is in the list of lines (do any lines exist) so no errors appear
    if lines is not None:

        # HoughLines returns theta values so it iterates through them all to find all lines
        for r_theta in lines:

            arr = num.array(r_theta[0], dtype=num.float64)

            r, theta = arr
            # Stores the value of cos(theta) in a
            a = num.cos(theta)

            # b stores the value of sin(theta) in b
            b = num.sin(theta)

            # x0 stores the value rcos(theta)
            x0 = a * r

            # y0 stores the value rsin(theta)
            y0 = b * r

            # x1 variable for the final line
            x1 = int(x0 + 1000 * (-b))

            # y1 variable for the final line
            y1 = int(y0 + 1000 * (a))

            # x2 variable for the final line
            x2 = int(x0 - 1000 * (-b))

            # y2 variable for the final line
            y2 = int(y0 - 1000 * (a))

            # cv2.line draws a line on the frame
            cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)

    # returns the frame with lines drawn
    return frame

# function for drawing contours
def contours(frame, rectangled):

    # finds the contours and hierarchy (order)
    contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # could be how I will find distance between contours
    if count == 0:
        vectorA = contours
        vectorB = contours

    # draws the contours on the frame
    cv2.drawContours(rectangled, contours, -1, (0, 255, 0), 3)

    # returns the final edited frame with contours
    return rectangled
