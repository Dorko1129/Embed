from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# 7.2 Colours
r = (255, 0, 0)   # red
w = (0, 0, 0)     # black / background

# 7.A Heart pattern (based on the hint)
heart_pixels = [
    w, w, w, w, w, w, w, w,
    w, r, r, w, w, r, r, w,
    r, r, r, r, r, r, r, r,
    r, r, r, r, r, r, r, r,
    w, r, r, r, r, r, r, w,
    w, w, r, r, r, r, w, w,
    w, w, w, r, r, w, w, w,
    w, w, w, w, w, w, w, w
]

# 7.4 Display heart
sense.set_pixels(heart_pixels)
sleep(5)
sense.clear()

