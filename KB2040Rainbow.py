#this is a KB2040 code for the KEEBOARS from adafruit 
#this is a rainbow animation for the on board neopixel

import time
import board
import neopixel
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.sequence import AnimationSequence

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1,brightness=0.5, auto_write=False)

rainbow = Rainbow(pixels, speed=0.1, period=2)
animations = AnimationSequence(
    rainbow)

while True:
    animations.animate()
