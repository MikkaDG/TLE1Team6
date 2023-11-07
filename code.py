import time
import random
from adafruit_circuitplayground import cp

while True:
    for i in range(len(cp.pixels)):
        # Genereer een willekeurige kleur.
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        cp.pixels[i] = color

    cp.pixels.show()
    cp.pixels.brightness = 0.1
    time.sleep(0.5)
