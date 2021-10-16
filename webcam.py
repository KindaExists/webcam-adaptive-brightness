
import cv2 as cv
import time

cv.namedWindow('webcam')
vc = cv.VideoCapture(0)

pause_time = 1

while True:
    # Get Webcam frame
    _, webcam_frame = vc.read()

    # Convert frame to grayscale
    gray_frame = cv.cvtColor(webcam_frame, cv.COLOR_BGR2GRAY)
    cv.imshow('webcam', gray_frame)

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
