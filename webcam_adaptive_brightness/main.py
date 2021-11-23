from webcam import Webcam
from brightness import Screen

min_ambient = 16
max_ambient = 235
min_display = 0
max_display = 100
threshold = 5

if __name__ == '__main__':
    wc = Webcam(0)
    sc = Screen()

    """
    Current Idea:
        Put both in seperate loop processes (thread/async)
        find a way to transfer data between them
        boom should finally work => PS: It didnt...
    """

    wc.open()
    ambient_brightness = wc.get_brightness()
    print(ambient_brightness)
    sc.update_brightness(ambient_brightness, min_ambient, max_ambient,
                         min_display, max_display)
    wc.release()
