
import screen_brightness_control as sbc
import cv2 as cv

cv.namedWindow('webcam')
vc = cv.VideoCapture(0)

current = sbc.get_brightness(display=0)
print(current)

while True:
    ret, frame = vc.read()
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv.imshow('webcam', frame)

    if cv.waitKey(5) == 27 or cv.waitKey(5) == 113:
        # "ESC" or "q" key
        break


vc.release()
cv.destroyWindow('webcam')
