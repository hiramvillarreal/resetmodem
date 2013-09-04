"""
This script does not function properly.  It hangs on GPIO.output (11, True)
 and pin 11 stays high, permanently, until the RPi is rebooted.

Here's the console message when the program is interrupted with ctl+c.

 Traceback (most recent call last):

  File "/home/pi/rpi/gpiooutput.py", line 26, in <module>
    toggle()
  File "/home/pi/rpi/gpiooutput.py", line 16, in toggle
    GPIO.setup(11, GPIO.OUT)
  File "/usr/local/lib/python2.7/dist-packages/RPi.GPIO-0.2.0-py2.7.egg/RPi/GPIO/__init__.py", line 102, in setup
 IOError: [Errno 13] Permission denied: '/sys/class/gpio/export'##
"""

 



import RPi.GPIO as GPIO
import time



def toggle():    

    GPIO.setup(11, GPIO.OUT)
    for i in range(1):
        GPIO.output(11, True)
        time.sleep(15)
        GPIO.output(11, False)
        time.sleep(240)


           
if __name__ == "__main__":
    toggle()
