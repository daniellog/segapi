#!/usr/bin/python
from time import sleep
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def exitEmulator(channel):
    print('exitEmulator')
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]

    for pid in pids:
        try:
            commandpath = open(os.path.join('/proc', pid, 'cmdline'), 'rb').read()
            if commandpath[0:24] == '/opt/retropie/emulators/':
                os.system('kill -QUIT %s' % pid)
                print('kill -QUIT %s' % pid)
        except IOError:
            continue
GPIO.add_event_detect(18, GPIO.RISING, callback=exitEmulator, bouncetime=500)

while True:
    sleep(10)
