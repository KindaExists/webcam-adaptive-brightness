#!/usr/bin/python
# -*- coding: utf-8 -*-
from webcam import Webcam
from display import Display
from configs_loader import Configs
from helper_classes import IntervalTimer, FilterMean

import os
import cv2 as cv

class Core:
    def __init__(self):
        # Load configuration/settings TOML file
        self.configs = Configs(os.path.abspath(os.path.dirname(__file__)+'/configs.toml'))

        # Initially set to a large negative float so that threshold
        # will always change on first update
        self.threshold_basis = -999999.0

    def setup_external(self):
        # Initialize webcam and display
        self.webcam = Webcam()

        self.webcam_device_name = self.configs.get_setting('device_name')
        self.webcam.open(self.webcam_device_name)
        self.capture = None
        if self.webcam.active_cam_in_list():
            self.capture = self.webcam.get_capture(compression_factor=2)

        self.display = Display(0)

    def setup_helpers(self):
        self.brightness_filter = FilterMean(max_points=(self.configs.get_setting('samples_per_update')))
        self.update_timer = IntervalTimer(self.configs.get_setting('update_interval'))

        loop_interval = self.configs.get_setting('update_interval') / self.configs.get_setting('samples_per_update')
        self.loop_timer = IntervalTimer(loop_interval)

    def update(self):
        if not self.webcam.active_cam_in_list():
            # Skip execution if webcam is unavailable
            return True

        # Captures another image from webcam/runs again
        # if loop timer is done
        if self.loop_timer.is_done():
            # Get frame
            # Measure brightness and insert into filter
            self.capture = self.webcam.get_capture(compression_factor=2)
            if self.capture is None:
                return

            self.measured_brightness = self.webcam.get_frame_brightness(self.capture)
            self.brightness_filter.insert(self.measured_brightness)

            # Updates screen brightness if update timer is done
            if self.update_timer.is_done():
                ambient_brightness = self.brightness_filter.get_mean()

                # Checks if threshold has been passed
                # before updating screen brightness
                threshold_diff = abs(ambient_brightness - self.threshold_basis)
                if threshold_diff >= self.configs.get_setting('threshold') * ((self.display.ambient_range[-1] / 100) + self.display.ambient_range[0]):
                    """
                    self.display.update_screen_brightness(
                        ambient_brightness,
                        self.configs.get_setting('ambient_percentages'),
                        self.configs.get_setting('screen_percentages')
                    )
                    """

                    # Sets new threshold basis
                    self.threshold_basis = ambient_brightness

            return True
        return False

    def release_external(self):
        self.webcam.release()
        self.webcam.close_windows()

    def update_helpers(self):
        self.brightness_filter.set_points(self.configs.get_setting('samples_per_update'))
        self.update_timer.set_interval(self.configs.get_setting('update_interval'))

        loop_interval = self.configs.get_setting('update_interval') / self.configs.get_setting('samples_per_update')
        self.loop_timer.set_interval(loop_interval)

    def get_last_ambient_brightness(self):
        return int(self.measured_brightness * (100 / (self.display.ambient_range[-1] - self.display.ambient_range[0])))

    def get_last_screen_brightness(self):
        return int(self.display.get_screen_brightness() * (100 / (self.display.screen_range[-1] - self.display.screen_range[0])))

    def get_converted_capture(self):
        cap = self.__get_last_capture()

        if not self.capture is None:
            h = cap.shape[0]
            ratio = 255 / h

            resized = cv.resize(cap, (int(cap.shape[1] * ratio),
                                    int(cap.shape[0] * ratio)))
            recolored = cv.cvtColor(resized, cv.COLOR_BGR2RGB)
            return recolored
        return None

    def update_webcam_device(self):
        setting_device_name = self.configs.get_setting('device_name')
        if self.webcam_device_name != setting_device_name:
            self.webcam_device_name = setting_device_name
            self.webcam.release()
            self.webcam.open(setting_device_name)

    def __get_last_capture(self):
        return self.capture

    def refresh_devices(self):
        self.webcam.release()
        self.webcam_device_name = self.configs.get_setting('device_name')
        self.webcam.open(self.webcam_device_name)
        self.capture = None
        if self.webcam.active_cam_in_list():
            self.capture = self.webcam.get_capture(compression_factor=2)
