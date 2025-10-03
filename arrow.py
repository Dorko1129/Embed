from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


# Colours
w = (0, 0, 0)       # black background
r = (255, 0, 0)     # green arrow

# Arrow patterns
up_arrow = [
    w,w,w,r,w,w,w,w,
    w,w,r,r,r,w,w,w,
    w,r,w,r,w,r,w,w,
    w,w,w,r,w,w,w,w,
    w,w,w,r,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w
]

down_arrow = [
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,r,w,w,w,w,
    w,w,w,r,w,w,w,w,
    w,r,w,r,w,r,w,w,
    w,w,r,r,r,w,w,w,
    w,w,w,r,w,w,w,w,
    w,w,w,w,w,w,w,w
]

right_arrow = [
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,r,w,w,w,w,
    w,w,w,w,r,w,w,w,
    w,r,r,r,r,r,w,w,
    w,w,w,w,r,w,w,w,
    w,w,w,r,w,w,w,w,
    w,w,w,w,w,w,w,w
]

left_arrow = [
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,r,w,w,w,w,
    w,w,r,w,w,w,w,w,
    w,r,r,r,r,r,w,w,
    w,w,r,w,w,w,w,w,
    w,w,w,r,w,w,w,w,
    w,w,w,w,w,w,w,w
]

middle_arrow = [
    w,w,w,w,w,w,w,w,
    w,w,r,r,r,r,w,w,
    w,r,w,w,w,w,r,w,
    w,r,w,r,r,w,r,w,
    w,r,w,r,r,w,r,w,
    w,r,w,w,w,w,r,w,
    w,w,r,r,r,r,w,w,
    w,w,w,w,w,w,w,w
]

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                sense.set_pixels(up_arrow)
            elif event.direction == "down":
                sense.set_pixels(down_arrow)
            elif event.direction == "left":
                sense.set_pixels(left_arrow)
            elif event.direction == "right":
                sense.set_pixels(right_arrow)
            elif event.direction == "middle":
                sense.set_pixels(middle_arrow)

            sleep(0.5)
            sense.clear()
