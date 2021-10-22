
import cv2 as cv
# import numpy as np

cv.namedWindow('webcam')
vc = cv.VideoCapture(0)

while True:
    # Gets webcam frame
    _, frame = vc.read()

    # Display grayscaled webcam output (for testing)
    cv.imshow('webcam', frame)

    # Converts image from BGR to Y'UV
    yuv_frame = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
    mean = cv.mean(yuv_frame)

    # Obtain the average Y' (Luma) of the image
    brightness = mean[0]

    # Code for exiting the webcam window
    # "ESC" or "q" key
    if cv.waitKey(5) == 27 or cv.waitKey(5) == 113:
        break

vc.release()
cv.destroyWindow('webcam')