# Python Script
# Name: gpiooutput.py
# Version: 0.5
# Author:  Efrain Olivares
# Date: Sept 14, 2013
# Function:  Power cycles Cox cable modem when called by another script, test_connectioon.py.

import RPi.GPIO as GPIO
import time



def toggle():    

    GPIO.setup(11, GPIO.OUT) 		# Selects GPIO pin 11 on RPi
    for i in range(1):
        GPIO.output(11, True)           # Pin 11 goes high, opening a NC relay and cutting power to modem
        time.sleep(15)                  # Keeps power off for 15 sec to allow modem to "die"
        GPIO.output(11, False)          # Pin 11 goes low to re-power the modem
        time.sleep(240)                 # 4 minute delay to allow modem to re-establish connection to Cox DOCSIS


           
if __name__ == "__main__":
    toggle()
