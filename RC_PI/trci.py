import pygame, sys
import RPi.GPIO as GPIO
from time import sleep, time
from pygame.locals import *

TRIG = 21
ECHO = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(6,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)

GPIO.output(23,0)
GPIO.output(5,0)
GPIO.output(6,0)
GPIO.output(13,0)
GPIO.output(19,0)
GPIO.output(26,0)

# Pygame screen dimensions
WIDTH = 100
HEIGH = 100

def forward(time):
 lon()
 GPIO.output(19,1)
 GPIO.output(6,1)
 sleep(time)
 GPIO.output(6,0)
 GPIO.output(19,0)
 lof()

def backward(time):
 lon()
 GPIO.output(26,1)
 GPIO.output(13,1)
 sleep(time)
 GPIO.output(26,0)
 GPIO.output(13,0)
 lof()

def left(time):
 GPIO.output(5,1)
 GPIO.output(19,1)
 GPIO.output(13,1)
 sleep(time)
 GPIO.output(19,0)
 GPIO.output(13,0)
 GPIO.output(5,0)

def right(time):
 GPIO.output(23,1)
 GPIO.output(6,1)
 GPIO.output(26,1)
 sleep(time)
 GPIO.output(6,0)
 GPIO.output(26,0)
 GPIO.output(23,0)

def lon():
 GPIO.output(23,1)
 GPIO.output(5,1)

def lof():
 GPIO.output(5,0)
 GPIO.output(23,0)

def message_display(text, screen):
    basicfont = pygame.font.SysFont('monospace', 10)
    text = basicfont.render(text, True, WHITE)
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery

    screen.fill(BLACK)
    screen.blit(text, textrect)
    pygame.display.update()

def measure_distance():
    GPIO.output(TRIG, 1)
    sleep(0.00001) #10uS
    GPIO.output(TRIG, 0)
    
    while GPIO.input(ECHO) == 0:
        pulse_start = time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance,2)
    return distance
    sleep(.5)

try:
        pygame.init()
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        windowSurface = pygame.display.set_mode((WIDTH, HEIGH), 0, 32)

        windowSurface.fill(BLACK)
        GPIO.output(TRIG, 0)
        sleep(2)

        x=0
        while True:
            message_display(str(measure_distance()), windowSurface)
            for event in pygame.event.get():
                    if event.type == QUIT:
                        GPIO.output(26,0)
                        GPIO.output(23,0)
                        GPIO.output(19,0)
                        GPIO.output(13,0)
                        GPIO.output(6,0)
                        GPIO.output(5,0)
                        GPIO.cleanup
                    if event.type == KEYDOWN:
                        key = event.key
                        if key == pygame.K_UP:
                            forward(.1)
                        elif key == pygame.K_DOWN:
                            backward(.1)
                        elif key == pygame.K_LEFT:
                            left(.1)
                        elif key == pygame.K_RIGHT:
                            right(.1)
                        elif key == pygame.K_f:
                            if x == 1:
                                lon()
                                x = 0
                            elif x == 0:
                                lof()
                                x = 1

except (KeyboardInterrupt):
	GPIO.output(26,0)
	GPIO.output(23,0)
	GPIO.output(21,0)
 	GPIO.output(19,0)
 	GPIO.output(13,0)
 	GPIO.output(6,0)
 	GPIO.output(5,0)
	GPIO.cleanup



GPIO.cleanup()
