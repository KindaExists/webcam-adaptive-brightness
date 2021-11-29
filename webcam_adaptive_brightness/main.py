from webcam import Webcam
import display
import cv2 as cv
import time

min_ambient = 16
max_ambient = 235
min_display = 0
max_display = 100
threshold = 5
change_period = 1   #in seconds

filter_vals = []
MAX_POINTS = 10


def filter_mean(new_val):
    global filter_vals

    if len(filter_vals) < MAX_POINTS:
        filter_vals.append(new_val)
    else:
        filter_values = filter_vals[1:] + [new_val]

    return sum(filter_values)/len(filter_values)


if __name__ == '__main__':
    wc = Webcam(0)
    wc.open()
    cap = wc.get_capture()
    wc.show_image('test', cap)

    timer_start = time.time()
    while True:
        cap = wc.get_capture()
        wc.show_image('test', cap)

        timer_now = time.time()
        time_interval = timer_now - timer_start

        if time_interval >= change_period:
            ambient_brightness = wc.get_brightness()
            timer_start = timer_now

            display.update_brightness(ambient_brightness, min_ambient, max_ambient, min_display, max_display)

        if cv.waitKey(20) == 27:
            break

    wc.release()
    wc.close_windows()
