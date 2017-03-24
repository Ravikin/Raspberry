#!/usr/bin/python
from pynput.keyboard import Key, Listener
import RPi.GPIO as GPIO
import time
import sys

PIN = 0

def init(PIN,BMODE):
	GPIO.setmode(GPIO.BMODE)
	print 'GPIO.setmode(GPIO.{0})'.format(BMODE)
	GPIO.setup(PIN, GPIO.OUT)
	print 'GPIO.setup({0},GPIO.OUT)'.format(PIN)

def LED_ON(key):
	GPIO.output(PIN,GPIO.HIGH)
	print "LED ON"
	time.sleep(.5)
#    print('{0} pressed'.format(key))

def LED_OFF(key):
	GPIO.output(PIN,GPIO.LOW)
	print "LED OFF"
	time.sleep(.5)
#    print('{0} release'.format(key))
	if key == Key.esc:
        # Stop listener
	GPIO.cleanup()
		return False

def main()
	try:
		os.system('clear')
		BM = raw_input("Podaj uklad GPIO: ")
		global PIN
		PIN = raw_input("Podaj numer pinu sterujacego: ")
		print "\n"
		init(PIN,BM)
		# Collect events until released
		with Listener(
		        on_press=LED_ON,
		        on_release=LED_OFF) as listener:
		    listener.join()
	except:
		GPIO.cleanup()
		print "\n"
		sys.exit()
if __name__ == '__main__':
	main()
