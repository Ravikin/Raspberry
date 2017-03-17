#!/usr/bin/python
import RPi.GPIO as GPIO
import time

def on_off():
	PIN_NR = raw_input("Podaj numer pinu sterujacego: ")
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(FALSE)
	GPIO.setup(PIN_NR,GPIO.out)
	while True:
		print "LED ON"
		GPIO.output(PIN_NR,GPIO.HIGH)
		time.sleep(.5)
		print "LED OFF"
		GPIO.output(PIN_NR,GPIO.LOW)
		time.sleep(.5)

def main():
	on_off()

if __name__ == '__main__':
	main()
