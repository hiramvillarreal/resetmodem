# Python Script
# Name: gpiooutput.py
# Version: 0.5
# Author:  Efrain Olivares
# Date: Sept 14, 2013
# Function:  Power cycles Cox cable modem when called by another script, test_connectioon.py.

import RPi.GPIO as GPIO
import time

def toggle():   
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(13, GPIO.OUT) 		# Selects GPIO pin 11 on RPi
    for i in range(1):
        GPIO.output(13, False)           # Pin 11 goes high, opening a NC relay and cutting power to modem
        time.sleep(15)                  # Keeps power off for 15 sec to allow modem to "die"
        GPIO.output(13, True)          # Pin 11 goes low to re-power the modem
        GPIO.cleanup() 
        time.sleep(24) 
           
if __name__ == "__main__":
    toggle()
