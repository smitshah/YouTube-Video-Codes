# Led Blinking using Relay and RPi
import RPi.GPIO as GPIO
from time import sleep

# Initialising the GPIO Pins
led1 = 14 
led2 = 4

def setup():
    GPIO.setwarnings(False)  # Do not show any warnings
    GPIO.setmode(GPIO.BCM)  # Programming the GPIO by BCM pin number

    GPIO.setup(led1, GPIO.OUT)
    GPIO.setup(led2, GPIO.OUT)

def logic00():
    GPIO.output(led1, True) # led1 OFF

    GPIO.output(led2, True) # led2 OFF

def logic01():
    GPIO.output(led1, True) # led1 OFF

    GPIO.output(led2, False) # led2 ON

def logic10():
    GPIO.output(led1, False) # led1 ON

    GPIO.output(led2, True) # led2 OFF

def logic11():
    GPIO.output(led1, False) # led1 ON

    GPIO.output(led2, False) # led2 ON

# To destroy/clean-up all the pins
def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        while True:
            print("00")
            logic00()
            sleep(2)
            print("01")
            logic01()
            sleep(2)
            print("10")
            logic10()
            sleep(2)
            print("11")
            logic11()
            sleep(2)
    except KeyboardInterrupt:
        print("Keyboard Interrupt Detected")
        destroy()