# Led Blinking using Switch and RPi
import RPi.GPIO as GPIO
from time import sleep

# Initialising the GPIO Pins
led = 4
switch = 17

def setup():
    GPIO.setmode(GPIO.BCM)   # Setting GPIO mode as BCM
    GPIO.setup(led, GPIO.OUT)  # Setting LED as output
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Setting Switch as input as pullup

def loop():
    while True:
        switch_state = GPIO.input(switch)
        
        if switch_state == False:
            print("Switch Pressed... Led High")
            GPIO.output(led, True)
        else:
            print("Led Blink")
            GPIO.output(led, True)
            sleep(0.1)
            GPIO.output(led, False)
            sleep(0.1)

def destroy():
	GPIO.output(led, False)     
	GPIO.cleanup()              

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Keyboard Interrupt Detected")
        destroy()