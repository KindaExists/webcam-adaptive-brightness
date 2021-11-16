
import cv2 as cv
import numpy as np


class Webcam:
    def __init__(self, cam_ref):
        self.vc = cv.VideoCapture()
        self.cam = cam_ref

    def __get_capture(self):
        self.vc.open(self.cam)

        # Saves exposure settings
        self.def_auto = self.vc.get(cv.CAP_PROP_AUTO_EXPOSURE)
        self.def_exposure = self.vc.get(cv.CAP_PROP_EXPOSURE)

        # Sets exposure to 100% and auto-exposure to 0%
        self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, 0.0)
        self.vc.set(cv.CAP_PROP_EXPOSURE, 1.0)

        # Converts image from BGR to Grayscale
        _, frame = self.vc.read()
        gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Returns exposure settings to original values
        self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, self.def_auto)
        self.vc.set(cv.CAP_PROP_EXPOSURE, self.def_exposure)

        self.vc.release()

        return gray_frame

    def get_brightness(self):
        frame = self.__get_capture()
        brightness = np.mean(frame)

        return brightness
