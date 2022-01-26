#add adafruit led animation to lib folder
import board
import neopixel

from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.color import JADE

# Update this to match the number of NeoPixel LEDs connected to your board.
num_pixels = 21

pixels = neopixel.NeoPixel(board.GP0, num_pixels)
pixels.brightness = 0.5

comet = Comet(pixels, speed=0.05, color=JADE, tail_length=5, bounce=True)

while True:
    comet.animate()
