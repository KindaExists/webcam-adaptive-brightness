
import cv2 as cv
import numpy as np

# Sets the maximum and minimum values for linear interpolation
max_luma = 255
min_luma = 0

max_display = 100
min_display = 0


def get_brightness(vc):
    # Gets brightness from webcam frame

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

    # Gets old exposure values
    original_auto = vc.get(cv.CAP_PROP_AUTO_EXPOSURE)
    original_exposure = vc.get(cv.CAP_PROP_EXPOSURE)

    # Sets exposure to 100% and disables auto-Exposure
    vc.set(cv.CAP_PROP_AUTO_EXPOSURE, float(0))
    vc.set(cv.CAP_PROP_EXPOSURE, float(1))

    while True:
        if cv.waitKey(5) == 27 or cv.waitKey(5) == 113:
            # Code for exiting the webcam window
            # "ESC" or "q" key
            break

        try:
            brightness = get_brightness(vc)
            new_display_brightness = round(np.interp(brightness,
                                           [min_luma, max_luma],
                                           [min_display, max_display]))
            
        except Exception:
            # Closes if webcam is not working
            print('ERROR: Webcam Disconnected')
            break

    # Returns exposure to original settings
    vc.set(cv.CAP_PROP_AUTO_EXPOSURE, original_auto)
    vc.set(cv.CAP_PROP_EXPOSURE, original_exposure)

    # Closes webcam input and display
    vc.release()
    cv.destroyWindow('webcam')
