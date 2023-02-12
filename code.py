import board
import neopixel

from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.blink import Blink
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.rainbow import Rainbow
from adafruit_led_animation.animation.rainbowchase import RainbowChase
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.animation.rainbowcomet import RainbowComet
from adafruit_led_animation.color import RED
from adafruit_led_animation.color import BLUE

# Variables
pixel_controller_pin = board.GP0
pixel_count = 28

pixels = neopixel.NeoPixel(
    pixel_controller_pin, pixel_count, auto_write=False, pixel_order=neopixel.RGB
)
pixels.brightness = 0.5

solid = Solid(pixels, color=BLUE)
blink = Blink(pixels, speed=0.5, color=RED)
comet = Comet(pixels, speed=0.01, color=BLUE, tail_length=10, bounce=True)
chase = Chase(pixels, speed=0.1, size=3, spacing=6, color=RED)
rainbow = Rainbow(pixels, speed=0.1, period=2)
rainbow_chase = RainbowChase(pixels, speed=0.1, size=5, spacing=3)
rainbow_comet = RainbowComet(pixels, speed=0.05, bounce=True)

animations = AnimationSequence(
    rainbow,
    comet,
    solid,
    rainbow_chase,
    blink,
    chase,
    advance_interval=3,
    auto_clear=True,
)

while True:
    animations.animate()
