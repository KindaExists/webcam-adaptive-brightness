import numpy as np
import wmi


def set_brightness(brightness):
    win = wmi.WMI(namespace='wmi')
    methods = win.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)


def ambient_to_display(brightness, min_ambient, max_ambient, min_display, max_display):
    new_display_brightness = round(np.interp(brightness, [min_ambient, max_ambient], [min_display, max_display]))
    return new_display_brightness


def update_brightness(ambient_brightness, min_ambient, max_ambient, min_display, max_display):
    new_brightness = ambient_to_display(ambient_brightness, min_ambient, max_ambient, min_display, max_display)

    set_brightness(new_brightness)
