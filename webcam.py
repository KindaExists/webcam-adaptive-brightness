
import cv2 as cv
# import numpy as np


def get_brightness(vc):
    # Gets webcam frame
    _, frame = vc.read()

    # Display grayscaled webcam output (for testing)
    cv.imshow('webcam', frame)

    # Converts image from BGR to Y'UV
    yuv_frame = cv.cvtColor(frame, cv.COLOR_BGR2YUV)
    mean = cv.mean(yuv_frame)

    # Obtain the average Y' (Luma) of the image
    brightness = mean[0]
    return brightness


if __name__ == '__main__':
    # This only runs if opened in this specific file

    # Setup for webcam input and display
    cv.namedWindow('webcam')
    vc = cv.VideoCapture(0)

    while True:
        if cv.waitKey(5) == 27 or cv.waitKey(5) == 113:
            # Code for exiting the webcam window
            # "ESC" or "q" key
            break

        try:
            print(get_brightness(vc))
        except Exception:
            print('ERROR: Webcam Disconnected')
            break

    # Closes webcam input and display
    vc.release()
    cv.destroyWindow('webcam')
