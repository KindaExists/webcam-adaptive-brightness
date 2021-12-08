import numpy as np
import wmi


class Display:
    def set_brightness(self, brightness):
        win = wmi.WMI(namespace='wmi')
        methods = win.WmiMonitorBrightnessMethods()[0]
        methods.WmiSetBrightness(brightness, 0)

    def _translate_from_ambient(self, brightness, minmax_ambient, minmax_display):
        new_display_brightness = round(np.interp(brightness,
            [minmax_ambient['min'], minmax_ambient['max']],
            [minmax_display['min'], minmax_display['max']]))
        return new_display_brightness

    def update_from_ambient(self, ambient_brightness, minmax_ambient, minmax_display):
        new_display_brightness = self._translate_from_ambient(ambient_brightness, minmax_ambient, minmax_display)
        self.set_brightness(new_display_brightness)

