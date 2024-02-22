import cv2
import numpy as num

def distance(frame, pointsList):

    counter = 0
    
    if pointsList is not None:
    
        for point in pointsList:
    
            point1 = point
    
            counter += 1
    
            point2 = pointsList[counter]
    
            # figure out how to calculate the distance between the two
