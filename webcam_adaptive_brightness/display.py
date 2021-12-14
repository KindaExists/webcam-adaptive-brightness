import numpy as np
import wmi


class Display:
    def __init__(self, screen_id=0):
        self.screen_id = screen_id
        self.level_range = self.get_screen_brightness_range()

        self.prev_brightness = -1
        self.was_overriden = False
        self.deviation_direction = 0

    def get_screen_brightness_range(self):
        win = wmi.WMI(namespace='wmi')
        monitor = win.WmiMonitorBrightness()[self.screen_id]
        level_range = (monitor.level[0], monitor.level[-1])

        return level_range

    def get_current_brightness(self):
        win = wmi.WMI(namespace='wmi')
        monitor = win.WmiMonitorBrightness()[self.screen_id]

        return monitor.CurrentBrightness

    def set_brightness(self, brightness):
        win = wmi.WMI(namespace='wmi')
        methods = win.WmiMonitorBrightnessMethods()[self.screen_id]
        methods.WmiSetBrightness(brightness, 0)

    def _translate_from_ambient(self, ambient_brightness, minmax_ambient):
        new_display_brightness = round(np.interp(ambient_brightness,
            [minmax_ambient['min'], minmax_ambient['max']],
            [self.level_range[0], self.level_range[-1]]))
        return new_display_brightness

    def update_from_ambient(self, ambient_brightness, minmax_ambient):
        cur_screen_brightness = self.get_current_brightness()
        new_screen_brightness = self._translate_from_ambient(ambient_brightness, minmax_ambient)

        if self.prev_brightness < 0:
            self.prev_brightness = new_screen_brightness
            self.set_brightness(new_screen_brightness)
            return

        # Checks if screen brightness matches with the screen brightness from the previous update
        # - If yes, that means the user changed the brightness manually
        # - If no, that means the user did not change the brightness between updates
        if self.prev_brightness != cur_screen_brightness and not self.was_overriden:
            self.was_overriden = True

            diff = cur_screen_brightness - self.prev_brightness
            self.deviation_direction = 1 if diff  > 0 else -1

        if self.was_overriden:
            cur_diff = new_screen_brightness - cur_screen_brightness
            cur_deviation_direction = 1 if cur_diff > 0 else -1

            if self.deviation_direction > 0 and cur_deviation_direction > 0:
                if new_screen_brightness >= cur_screen_brightness:
                    self.was_overriden = False
                    self.deviation_direction = 0

            elif self.deviation_direction < 0 and cur_deviation_direction < 0:
                if new_screen_brightness <= cur_screen_brightness:
                    self.was_overriden = False
                    self.deviation_direction = 0

        # Does not update prev_brightness or screen brightness if manual override was done
        if not self.was_overriden:
            self.prev_brightness = new_screen_brightness
            self.set_brightness(new_screen_brightness)
