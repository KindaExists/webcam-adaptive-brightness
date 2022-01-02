import cv2 as cv


class Webcam:
    def __init__(self):
        self.vc = cv.VideoCapture()

    def get_brightness(self, compression_factor=1):
        frame = self.get_gray(compression_factor)
        brightness = cv.mean(frame)[0]

        return brightness

    def get_gray(self, compression_factor=1):
        # Converts image from BGR to Grayscale (Y')
        cap = self.get_capture(compression_factor)
        gray = cv.cvtColor(cap, cv.COLOR_BGR2GRAY)

        return gray

    def get_capture(self, compression_factor=1):
        _, frame = self.vc.read()
        compressed = cv.resize(frame, (frame.shape[1] // compression_factor,
                                       frame.shape[0] // compression_factor))
        return compressed

    def open(self, cam_id):
        self.vc.open(cam_id)

        # Saves exposure settings
        self.def_auto = self.vc.get(cv.CAP_PROP_AUTO_EXPOSURE)
        self.def_exposure = self.vc.get(cv.CAP_PROP_EXPOSURE)

        # Sets exposure to 100% and auto-exposure to 0%
        self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, 0.0)
        self.vc.set(cv.CAP_PROP_EXPOSURE, 1.0)

    def release(self):
        self.vc.set(cv.CAP_PROP_AUTO_EXPOSURE, self.def_auto)
        self.vc.set(cv.CAP_PROP_EXPOSURE, self.def_exposure)

        self.vc.release()

    def show_image(self, window_name, frame):
        cv.imshow(window_name, frame)

    def close_windows(self):
        cv.destroyAllWindows()
