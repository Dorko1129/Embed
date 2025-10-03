from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Colors
r = (255, 0, 0)   # red
w = (0, 0, 0)     # black (background)

# Heart pattern (from earlier task)
heart = [
    w,w,w,w,w,w,w,w,
    w,r,r,w,w,r,r,w,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    w,r,r,r,r,r,r,w,
    w,w,r,r,r,r,w,w,
    w,w,w,r,r,w,w,w,
    w,w,w,w,w,w,w,w
]

# 10.2 Functions
def red():
    sense.clear(255, 0, 0)

def blue():
    sense.clear(0, 0, 255)

def green():
    sense.clear(0, 255, 0)

def yellow():
    sense.clear(255, 255, 0)

# 10.A Blinking red heart
def blinking_heart():
    for i in range(5):        # blink 5 times
        sense.set_pixels(heart)
        sleep(0.5)
        sense.clear()
        sleep(0.5)

# 10.3 Define trigger events
sense.stick.direction_up = blinking_heart   # modified
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear

# 10.4 Keep running
while True:
    pass
