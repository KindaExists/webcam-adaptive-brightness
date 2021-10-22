
import cv2 as cv
# import numpy as np

cv.namedWindow('webcam')
vc = cv.VideoCapture(0)

pause_time = 1

while True:
    # Gets webcam frame
    _, frame = vc.read()

    # Display grayscaled webcam output (for testing)
    cv.imshow('webcam', frame)

    yuv_frame = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
    mean = cv.mean(yuv_frame)
    brightness = mean[0]

    print(brightness)

    if cv.waitKey(5) == 27 or cv.waitKey(5) == 113:
        # "ESC" or "q" key
        break

vc.release()
cv.destroyWindow('webcam')
