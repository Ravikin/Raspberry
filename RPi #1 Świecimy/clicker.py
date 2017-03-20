#import RPi.GPIO as GPIO
import time
import os
import sys

def init(PIN,BMODE):
	#GPIO.setmode(GPIO.BMODE)
	print 'GPIO.setmode(GPIO.{0})'.format(BMODE)
	#GPIO.setup(PIN, GPIO.OUT)
	print 'GPIO.setup({0},GPIO.OUT)'.format(PIN)

def LED_ON(PIN):
#	GPIO.out(PIN,GPIO.HIGH)
	print "LED ON"
	time.sleep(.5)

def LED_OFF(PIN):
#	GPIO.OUT(PIN,GPIO.HIGH)
	print "LED OFF"
	time.sleep(.5)

def main():
	try:
		os.system('clear')
		BM = raw_input("Podaj uklad GPIO: ")
		PIN = raw_input("Podaj numer pinu sterujacego: ")
		print '\n'
		init(PIN,BM)
	
		while True:
			LED_ON(PIN)
			sys.stdin.read(1)
			LED_OFF(PIN)
			sys.stdin.read(1)
	
	#	GPIO.cleanup()
	except KeyboardInterrupt:
	#	GPIO.cleanup()
		print "Do widzenia..."
		sys.exit()
	
if __name__ == '__main__':
	main()
