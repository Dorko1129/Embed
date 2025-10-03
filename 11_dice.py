from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

# 11.3 Colours
o = (0, 0, 0)     # off
b = (0, 0, 255)   # blue

# 11.4 Dice face patterns
one_img = [
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o
]

two_img = [
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,o,o,o
]

three_img = [
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,b,b,o,o,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,b,b,o,
    o,o,o,o,o,o,o,o
]

four_img = [
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o,
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o
]

five_img = [
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,b,b,o,o,o,
    o,o,o,b,b,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o
]

six_img = [
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o,
    o,o,o,o,o,o,o,o,
    o,b,b,o,o,b,b,o,
    o,b,b,o,o,b,b,o
]

# 11.5 Event handler with rolling effect for Task 12
def number_gen(event):
    if event.action == "pressed":
        # Rolling effect: 3 seconds at 10 times per second
        for _ in range(30):
            val = random.randint(1,6)
            if val == 1:
                sense.set_pixels(one_img)
            elif val == 2:
                sense.set_pixels(two_img)
            elif val == 3:
                sense.set_pixels(three_img)
            elif val == 4:
                sense.set_pixels(four_img)
            elif val == 5:
                sense.set_pixels(five_img)
            elif val == 6:
                sense.set_pixels(six_img)
            sleep(0.1)

        # Final result
        val = random.randint(1,6)
        print("Final dice result:", val)
        if val == 1:
            sense.set_pixels(one_img)
        elif val == 2:
            sense.set_pixels(two_img)
        elif val == 3:
            sense.set_pixels(three_img)
        elif val == 4:
            sense.set_pixels(four_img)
        elif val == 5:
            sense.set_pixels(five_img)
        elif val == 6:
            sense.set_pixels(six_img)
        sleep(2)
        sense.clear()

# 11.6 Trigger event
sense.stick.direction_middle = number_gen

# 11.7 Keep program running
while True:
    pass

