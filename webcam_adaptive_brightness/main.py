from webcam import Webcam
from configs_loader import Configs
from display import Display
import cv2 as cv
from helper_classes import IntervalTimer, FilterMean
import os


def run():
    # Load configuration/settings JSON file
    configs = Configs(os.path.abspath(os.path.dirname(__file__)+'/configs.toml'))

    # Initialize webcam and open stream
    try:
        wc = Webcam()
        wc.open(configs.device)
        wc.show_image('Window', wc.get_gray(compression_factor=2))
    except Exception as e:
        print("Webcam not found! Please check and make sure it's working")
        print(e)
        return

    try:
        display = Display(0)
    except Exception as e:
        print('Display not compatible. This program only works ' +
              'with Windows 10 laptops and displays.')
        print(e)
        return

    # Initially set to a large negative float so that threshold
    # will always change on first update
    threshold_basis = -999999.0

    # Initialize filter object
    # Specific formula used to compute "max_points" was added to avoid
    # there not being enough steps to adjust filter
    brightness_filter = FilterMean(max_points=(configs.samples_per_update))
    try:
        # Start timers
        update_timer = IntervalTimer(configs.update_interval)
        loop_interval = configs.update_interval / configs.samples_per_update
        loop_timer = IntervalTimer(loop_interval)

        while True:
            # Captures another image from webcam/runs again
            # if loop timer is done
            if loop_timer.is_done():
                # Get grayscaled image and display on-screen
                wc.show_image('Window', wc.get_gray(compression_factor=2))

                # Measure brightness and insert into filter
                measured_brightness = wc.get_brightness(compression_factor=2)
                brightness_filter.insert(measured_brightness)

                # Updates screen brightness if update timer is done
                if update_timer.is_done():
                    ambient_brightness = brightness_filter.get_mean()
                    print(ambient_brightness)

                    # Checks if threshold has been passed
                    # before updating screen brightness
                    threshold_diff = abs(ambient_brightness - threshold_basis)
                    if threshold_diff >= configs.threshold:
                        display.update_from_ambient(ambient_brightness,
                                                    configs.ambient)

                        # Sets new threshold
                        threshold_basis = ambient_brightness

            # TEMPORARY: Await "Esc" key response to close program
            if cv.waitKey(20) == 27:
                break

            # Pause execution of program for a short bit to reduce load
            # time.sleep(0.1)
    except Exception as e:
        print(e)
    finally:
        wc.release()
        wc.close_windows()


if __name__ == '__main__':
    run()
