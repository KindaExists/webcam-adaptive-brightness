import numpy as np
import wmi


def _set_screen_brightness(brightness):
    win = wmi.WMI(namespace='wmi')
    methods = win.WmiMonitorBrightnessMethods()[0]
    methods.WmiSetBrightness(brightness, 0)

def _translate_ambient_to_display(brightness, minmax_ambient, minmax_display):
    new_display_brightness = round(np.interp(brightness,
        [minmax_ambient['min'], minmax_ambient['max']],
        [minmax_display['min'], minmax_display['max']]))
    return new_display_brightness

def update_brightness(ambient_brightness, minmax_ambient, minmax_display):
    new_display_brightness = _translate_ambient_to_display(ambient_brightness, minmax_ambient, minmax_display)
    _set_screen_brightness(new_display_brightness)


