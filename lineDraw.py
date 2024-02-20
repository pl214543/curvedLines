# import required libraries
import cv2
import numpy as num

def drawing(frame, lines):
    if lines is not None:
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
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

    return frame

def contours(frame, rectangled):
    contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(rectangled, contours, -1, (0, 255, 0), 3)
    return rectangled
