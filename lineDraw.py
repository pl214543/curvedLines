# import required libraries
import cv2
import numpy as num

# import drawing function

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

    midpointList = []

    # draws the contours on the frame
    # cv2.drawContours(rectangled, contours, -1, (0, 255, 0), 3)

    for contour in contours:

        approx = cv2.approxPolyDP(contour, 0.009 * cv2.arcLength(contour, True), True)

        cv2.drawContours(rectangled, [approx], 0, (0, 0, 255), 5)

        n = approx.ravel()
        i = 0

        for j in n:
            if (i % 2 == 0):
                x = n[i]
                y = n[i + 1]

                # String containing the co-ordinates.
                string = str(x) + " " + str(y)

                if (i == 0):
                    # text on topmost co-ordinate.
                    cv2.putText(rectangled, "Arrow tip", (x, y),
                                cv2.FONT_HERSHEY_COMPLEX , 0.5, (255, 0, 0))
                else:
                    midpointList.append(string)
            i = i + 1

        # returns the final edited frame with contours
    return rectangled
