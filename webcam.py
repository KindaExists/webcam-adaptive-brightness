
import cv2 as cv
import numpy as np
import time

cv.namedWindow('webcam')
vc = cv.VideoCapture(0)

pause_time = 1

# ? Consider making this an async function
while True:
    # Gets webcam frame
    _, webcam_frame = vc.read()

    # Converts webcam frame to grayscale
    gray_frame = cv.cvtColor(webcam_frame, cv.COLOR_BGR2GRAY)

    # Display grayscaled webcam output (for testing)
    cv.imshow('webcam', gray_frame)

    # Gets average (HSV) value of frame
    # ! Consider not using the average value
    # ! Averaging treats all values the same
    # ! So white (255) will be treated the same as lower values
    # ? Look into using the "dominant" value
    avg_val_per_row = np.average(gray_frame, axis=0)
    avg_val = np.average(avg_val_per_row, axis=0)
    print(avg_val)

    if cv.waitKey(5) == 27 or cv.waitKey(5) == 113:
        # "ESC" or "q" key
        break

    # Pause for length in seconds, pause time will be defined by the user
    # ! Issue: "time.sleep" causes a freeze
    # * Potential Solution: Do pauses based on time since last timeout
    # *                     to avoid freezing the entire algorithm
    time.sleep(pause_time)


vc.release()
cv.destroyWindow('webcam')
