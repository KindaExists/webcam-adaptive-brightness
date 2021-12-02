from webcam import Webcam
from settings import Settings
import display
import cv2 as cv
import time

settings_path = './webcam_adaptive_brightness/settings.json'


class filter_mean:
    def __init__(self, max_points=10):
        self.vals = []
        self.N = 0
        self.max_points = max_points

    def insert(self, new_val):
        if self.N < self.max_points:
            self.vals.append(new_val)
            self.N += 1
        else:
            self.vals = self.vals[1:] + [new_val]

    def set_points(self, max_points=10):
        self.max_points = max_points

    def get_mean(self):
        return sum(self.vals)/self.N


def run():
    # Load configuration/settings JSON file
    configs = Settings(settings_path)

    # Initialize webcam and open stream
    wc = Webcam()
    wc.open(configs.device)

    capture = wc.get_gray()
    wc.show_image('Window', capture)

    # Initialize filter object
    brightness_filter = filter_mean(max_points=12)
    try:
        # Start timers by setting them to the current time
        loop_timer_start = time.time()
        update_timer_start = time.time()
        while True:
            # Check loop timer and find current length
            loop_timer_now = time.time()
            loop_timer_length = loop_timer_now - loop_timer_start

            # Updates values and reads camera after loop timer is done
            if configs.loop_interval <= loop_timer_length:
                # Get grayscaled image and display on-screen
                cap = wc.get_gray()
                wc.show_image('Window', cap)

                # Measure brightness and insert into filter
                measured_brightness = wc.get_brightness()
                brightness_filter.insert(measured_brightness)

                # Check update timer and find current length
                update_timer_now = time.time()
                update_timer_length = update_timer_now - update_timer_start

                # Updates screen brightness if update timer is done
                if configs.update_interval <= update_timer_length:
                    # Resets update timer by setting start time to current time
                    update_timer_start = update_timer_now
                    ambient_brightness = brightness_filter.get_mean()

                    display.update_brightness(ambient_brightness, configs.ambient, configs.display)

                # Resets loop timer by setting start time to current time
                loop_timer_start = loop_timer_now

            if cv.waitKey(20) == 27:
                break

            # Sleep program for a short bit to reduce load
            time.sleep(0.1)
    except Exception as e:
        print(e)
    finally:
        wc.release()
        wc.close_windows()


if __name__ == '__main__':
    run()
