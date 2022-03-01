#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import wmi


class Display:
    def __init__(self, screen_id=0):
        self.screen_id = screen_id
        self.screen_range = self.__get_screen_brightness_range()
        self.ambient_range = (0.0, 255.0)

    def __get_screen_brightness_range(self):
        win = wmi.WMI(namespace='wmi')
        monitor = win.WmiMonitorBrightness()[self.screen_id]
        level_range = (monitor.level[0], monitor.level[-1])

        return level_range

    def get_screen_brightness(self):
        win = wmi.WMI(namespace='wmi')
        monitor = win.WmiMonitorBrightness()[self.screen_id]
        return monitor.CurrentBrightness

    def __set_screen_brightness(self, brightness):
        win = wmi.WMI(namespace='wmi')
        methods = win.WmiMonitorBrightnessMethods()[self.screen_id]
        methods.WmiSetBrightness(brightness, 0)

    def __translate_from_ambient(self, ambient_brightness, minmax_ambient, minmax_screen):
        new_display_brightness = round(np.interp(
            ambient_brightness,
            [minmax_ambient[0], minmax_ambient[-1]],
            [minmax_screen[0], minmax_screen[-1]]))
        return new_display_brightness

    def __convert_percent_range(self, minmax_range, level_range):
        a_end = (minmax_range[0] * level_range[-1] / 100) + level_range[0]
        b_end = (minmax_range[-1] * level_range[-1] / 100) + level_range[0]
        return (a_end, b_end)

    def update_screen_brightness(self, ambient_value, minmax_percent_ambient, minmax_percent_screen):
        minmax_ambient = self.__convert_percent_range(minmax_percent_ambient, self.ambient_range)
        minmax_screen = self.__convert_percent_range(minmax_percent_screen, self.screen_range)

        new_screen_brightness = self.__translate_from_ambient(
            ambient_value,
            minmax_ambient,
            minmax_screen,
        )
        self.__set_screen_brightness(new_screen_brightness)
