# Wlacza i wylacza LED na podanym przy starcie nr. GPIO. 'a' włącza | 'b' wyłącza
import RPi.GPIO as GPIO
import time
import os
import sys

def init(PIN,BMODE):
	GPIO.setmode(GPIO.BMODE)
	print 'GPIO.setmode(GPIO.{0})'.format(BMODE)
	GPIO.setup(PIN, GPIO.OUT)
	print 'GPIO.setup({0},GPIO.OUT)'.format(PIN)

def LED_ON(PIN):
	GPIO.output(PIN,GPIO.HIGH)
	print "LED ON"
	time.sleep(.05)

def LED_OFF(PIN):
	GPIO.output(PIN,GPIO.HIGH)
	print "LED OFF"
	time.sleep(.05)

def main():
	try:
		os.system('clear')
		BM = raw_input("Podaj uklad GPIO: ")
		PIN = raw_input("Podaj numer pinu sterujacego: ")
		print '\n'
		init(PIN,BM)
	
		while True:
			x = raw_input()
			if x == 'a':
				LED_ON(PIN)
			elif x == 'b':
				LED_OFF(PIN)
			else:
				break
		GPIO.cleanup()
	except:
		GPIO.cleanup()
	print "\nDo widzenia..."
	sys.exit()
if __name__ == '__main__':
	main()
