import RPi.GPIO as GPIO
from time import sleep
#imports the GPIO library as GPIO
#imports the sleep lib from the time lib?

GPIO.setmode(GPIO.BOARD)
# set to the RB PI layout
GPIO.setup(13, GPIO.OUT)
# set pin 13 as an output

while True:
    GPIO.output(13, True)
    print 'LED on'
    sleep(4)
    GPIO.output(13, False)
    print 'LED off'
    sleep(4)
