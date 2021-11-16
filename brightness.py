import screen_brightness_control as sbc
import numpy as np


class Screen:
    def __ambient_to_display(self, brightness, min_ambient, max_ambient,
                             min_display, max_display):
        new_display_brightness = round(np.interp(brightness,
                                                 [min_ambient, max_ambient],
                                                 [min_display, max_display]))
        return new_display_brightness

    def __set_brightness(self, brightness):
        sbc.fade_brightness(brightness, interval=0, blocking=False)

    def update_brightness(self, ambient_brightness,
                          min_ambient, max_ambient,
                          min_display, max_display):
        new_brightness = self.__ambient_to_display(ambient_brightness,
                                                   min_ambient, max_ambient,
                                                   min_display, max_display)
        self.__set_brightness(new_brightness)
