# import required libraries
import cv2
import numpy as num
from parallelCheck import findParallels

# import distance function
# from distanceDetect import distance

# function for drawing contours
def contours(frame, addRectangle):

    # finds the contours and hierarchy (order)
    contours, hierarchy = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # https://stackoverflow.com/questions/32669415/opencv-ordering-a-contours-by-area-python
    contoursSorted = sorted(contours, key=lambda x: cv2.contourArea(x))

    # creates lists of points
    pointsList = []
    midPoints1 = []
    midPoints = []

    # creates variables for averages.
    averageX = 0
    averageY = 0

    # gets each contour
    for contour in contours:

        # draws each contour
        cv2.drawContours(addRectangle, [contour], 0, (0, 255, 0), 10)

        # use fill poly?

        n = contour.ravel()
        i = 0

        #  https://www.geeksforgeeks.org/find-co-ordinates-of-contours-using-opencv-python/
        # goes through every point in the contour
        for j in n:
            if i % 2 == 0:
                x = n[i]
                y = n[i + 1]

                # appends the points to pointsList
                pointsList.append([x, y])

            # for iteration
            i = i + 1

    # iterates through contours again
    for j in contours:
        
        # tries to get the averages
        for i in range(len(pointsList)):
            averageX += pointsList[i][0]
            averageY += pointsList[i][1]

        averageX = averageX / len(pointsList)
        averageY = averageY / len(pointsList)

    # adds averages to midpoint list
    midPoints.append([int(averageX), int(averageY)])

    # draws the center line
    addRectangle = cv2.polylines(addRectangle, [num.array(midPoints)],
                          True, (255, 0, 0), 5)

    return addRectangle
