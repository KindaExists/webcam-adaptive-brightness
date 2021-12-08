from webcam import Webcam
from settings import Settings
from display import Display
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


class Timer:
    def __init__(self, timer_interval):
        self.interval = timer_interval
        self.start()

    def start(self):
        self.start_time = time.time()

    def get_passed(self):
        current_time = time.time()
        return current_time - self.start_time

    def is_done(self):
        if self.get_passed() >= self.interval:
            self.start()
            return True

        return False


def run():
    # Load configuration/settings JSON file
    configs = Settings(settings_path)

    # Initialize webcam and open stream
    try:
        wc = Webcam()
        wc.open(configs.device)
        wc.show_image('Window', wc.get_gray())
    except Exception as e:
        print("Webcam not found! Please check and make sure it's working")
        print(e)
        return

    try:
        display = Display()
    except Exception as e:
        print('Display not compatible. This program only works with Windows 10 laptops and displays.')
        print(e)
        return

    # Initially set to a large negative float so that threshold
    # will always change on first update
    threshold_basis = -999999.0

    # Initialize filter object
    # Specific formula used to compute "max_points" was added to avoid
    # there not being enough steps to adjust filter
    brightness_filter = filter_mean(max_points=(configs.update_interval // configs.loop_interval))
    try:
        # Start timers
        update_timer =  Timer(configs.update_interval)
        loop_timer = Timer(configs.loop_interval)

        while True:
            # Captures another image from webcam/runs again if loop timer is done
            if loop_timer.is_done():
                # Get grayscaled image and display on-screen
                wc.show_image('Window', wc.get_gray())

                # Measure brightness and insert into filter
                measured_brightness = wc.get_brightness()
                brightness_filter.insert(measured_brightness)

                # Updates screen brightness if update timer is done
                if update_timer.is_done():
                    ambient_brightness = brightness_filter.get_mean()
                    print(ambient_brightness)

                    # Checks if threshold has been passed before updating screen brightness
                    if abs(ambient_brightness - threshold_basis) >= configs.threshold:
                        display.update_from_ambient(ambient_brightness, configs.ambient, configs.display)

                        # Sets new threshold
                        threshold_basis = ambient_brightness

            # TEMPORARY: Await "Esc" key response to close program
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
