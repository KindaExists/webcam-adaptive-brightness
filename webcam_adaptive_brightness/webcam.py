#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2 as cv
from pygrabber.dshow_graph import FilterGraph

class Webcam:
    def __init__(self):
        self.vc = cv.VideoCapture()

        self.active_cam_name = None
        self.graph = FilterGraph()

        self.cam_listed = False

    def get_frame_brightness(self, frame):
        gray = self.convert_gray(frame)
        brightness = cv.mean(gray)[0]
        return brightness

    def convert_gray(self, frame):
        # Converts image from BGR to Grayscale (Y')
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        return gray

    def get_capture(self, compression_factor=1):
        if self.active_cam_in_list():
            self.has_opened = True
            ret_val, frame = self.vc.read()
            if ret_val:
                compressed = cv.resize(frame, (frame.shape[1] // compression_factor,
                                       frame.shape[0] // compression_factor))
                return compressed
        self.has_opened = False
        return None

    def open(self, cam_name):
        self.active_cam_name = cam_name
        try:
            cam_id = self.list_cameras().index(cam_name)
        except ValueError:
            cam_id = 0

        self.vc.open(cam_id)

    def release(self):
        self.has_opened = False
        self.active_cam_name = None
        self.vc.release()

    def show_image(self, window_name, frame):
        cv.imshow(window_name, frame)

    def close_windows(self):
        cv.destroyAllWindows()

    def list_cameras(self):
        return self.graph.get_input_devices()

    def active_cam_in_list(self):
        return self.active_cam_name in self.list_cameras()
