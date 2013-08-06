##    LED BLINKER   ##
#  LED Blinker on Pin 11 (Stolen from "Raspberry Pi User Guide" pg 194)
#  Ver. 0.1
#  August 5, 2013
#  J. Hobson
#  Just prior to this, I imported "raspberry-gpio-python"library  (ibid pg 190)


import RPi.GPIO as GPIO
import time
GPIO.setup(11, GPIO.OUT)
while True:
    GPIO.output(11, True)
    time.sleep(2)
    GPIO.output(11, False)
    time. sleep(2)