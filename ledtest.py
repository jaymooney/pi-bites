#!/usr/bin/env python

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
switchpin = 25
redpin = 18
greenpin = 22
bluepin = 23

GPIO.setup(redpin, GPIO.OUT)
GPIO.setup(greenpin, GPIO.OUT)
GPIO.setup(bluepin, GPIO.OUT)
GPIO.setup(switchpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

color = 0

def handleButton(channel):
	global color
	color = (color + 1) % 3
	print "color: %d" % color
	GPIO.output(redpin, color != 0)
	GPIO.output(greenpin, color != 1)
	GPIO.output(bluepin, color != 2)


if __name__ == '__main__':
	try:
		print 'ctrl-c to quit'
		GPIO.add_event_detect(switchpin, GPIO.FALLING, callback=handleButton, bouncetime=200)
		while True:
			pass
	finally:
		GPIO.cleanup()

