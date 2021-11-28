
import cv2 as cv


class Webcam:
    def __init__(self, cam_ref):
        self.vc = cv.VideoCapture()
        self.cam = cam_ref

    def get_brightness(self):
        frame = self.get_values()
        brightness = cv.mean(frame)[0]

        return brightness

    def get_values(self):
        # Converts image from BGR to Grayscale (Y')
        cap = self.get_capture(exposure=False)
        gray = cv.cvtColor(cap, cv.COLOR_BGR2GRAY)

        return gray

    def get_capture(self, exposure=True):
        if not exposure:
            # Saves exposure settings
            def_auto = self.vc.get(cv.CAP_PROP_AUTO_EXPOSURE)
            def_exposure = self.vc.get(cv.CAP_PROP_EXPOSURE)

            # Sets exposure to 100% and auto-exposure to 0%
            self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, 0.0)
            self.vc.set(cv.CAP_PROP_EXPOSURE, 1.0)

        _, frame = self.vc.read()

        if not exposure:
            # Reverts exposure settings to original values
            self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, def_auto)
            self.vc.set(cv.CAP_PROP_EXPOSURE, def_exposure)

        return frame

    def open(self):
        self.vc.open(self.cam)

    def release(self):
        self.vc.release()

    def show_image(self, window_name, frame):
        cv.imshow(window_name, frame)

    def close_windows(self):
        cv.destroyAllWindows()
