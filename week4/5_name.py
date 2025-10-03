from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

def random_colour():
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)

sense.show_letter("z", random_colour())
sleep(1)
sense.show_letter("s", random_colour())
sleep(1)
sense.show_letter("o", random_colour())
sleep(1)
sense.show_letter("m", random_colour())
sleep(1)
sense.show_letter("b", random_colour())
sleep(1)
sense.show_letter("o", random_colour())
sleep(1)
sense.show_letter("r", random_colour())
sleep(1)

sense.clear()
