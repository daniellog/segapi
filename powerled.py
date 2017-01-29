#!/usr/bin/python
from time import sleep
import os
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(15, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
GPIO.output(15,True) ## Turn on GPIO pin 7


