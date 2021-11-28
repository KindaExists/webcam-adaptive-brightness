import screen_brightness_control as sbc
import numpy as np


def ambient_to_display(brightness, min_ambient, max_ambient,
                       min_display, max_display):
    new_display_brightness = round(np.interp(brightness,
                                             [min_ambient, max_ambient],
                                             [min_display, max_display]))
    return new_display_brightness


def set_brightness(brightness):
    sbc.set_brightness(brightness)


def update_brightness(ambient_brightness,
                      min_ambient, max_ambient,
                      min_display, max_display):
    new_brightness = ambient_to_display(ambient_brightness,
                                        min_ambient, max_ambient,
                                        min_display, max_display)
    set_brightness(new_brightness)
