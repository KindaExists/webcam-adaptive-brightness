
import cv2 as cv
import numpy as np


class Webcam:
    def __init__(self, cam_ref):
        self.vc = cv.VideoCapture()
        self.cam = cam_ref

    def get_brightness(self):
        frame = self.__get_values()
        brightness = np.mean(frame)

        return brightness

    def get_capture(self):
        _, frame = self.vc.read()
        return frame

    def open(self):
        self.vc.open(self.cam)

    def release(self):
        self.vc.release()

    def __get_values(self):
        # Saves exposure settings
        def_auto = self.vc.get(cv.CAP_PROP_AUTO_EXPOSURE)
        def_exposure = self.vc.get(cv.CAP_PROP_EXPOSURE)

        # Sets exposure to 100% and auto-exposure to 0%
        self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, 0.0)
        self.vc.set(cv.CAP_PROP_EXPOSURE, 1.0)

        # Converts image from BGR to Grayscale
        cap = self.get_capture()
        gray = cv.cvtColor(cap, cv.COLOR_BGR2GRAY)

        # Returns exposure settings to original values
        self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, def_auto)
        self.vc.set(cv.CAP_PROP_EXPOSURE, def_exposure)

        return gray
