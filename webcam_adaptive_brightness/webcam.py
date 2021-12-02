
import cv2 as cv


class Webcam:
    def __init__(self, cam_ref):
        self.vc = cv.VideoCapture()
        self.cam = cam_ref

    def get_brightness(self):
        frame = self.get_gray()
        brightness = cv.mean(frame)[0]

        return brightness

    def get_gray(self):
        # Converts image from BGR to Grayscale (Y')
        cap = self.get_capture()
        gray = cv.cvtColor(cap, cv.COLOR_BGR2GRAY)

        return gray

    def get_capture(self):
        _, frame = self.vc.read()

        return frame

    def open(self, exposure_disabled=True):
        self.vc.open(self.cam)

        if exposure_disabled:
            # Saves exposure settings
            self.def_auto = self.vc.get(cv.CAP_PROP_AUTO_EXPOSURE)
            self.def_exposure = self.vc.get(cv.CAP_PROP_EXPOSURE)

            # Sets exposure to 100% and auto-exposure to 0%
            self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, 0.0)
            self.vc.set(cv.CAP_PROP_EXPOSURE, 1.0)

    def release(self, exposure_disabled=True):
        self.vc.release()

        if exposure_disabled:
            # Reverts exposure settings to original values
            # self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, self.def_auto)
            # self.vc.set(cv.CAP_PROP_EXPOSURE, self.def_exposure)

            # TEMPORARY SETTERS, these are specific to my system
            self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, 0.0)
            self.vc.set(cv.CAP_PROP_EXPOSURE, -6.0)

    def show_image(self, window_name, frame):
        cv.imshow(window_name, frame)

    def close_windows(self):
        cv.destroyAllWindows()
