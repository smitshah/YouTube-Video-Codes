# Led Blinking using Switch and RPi

import RPi.GPIO as GPIO
from time import sleep

def setup():
    GPIO.setwarnings(False)  # Do not show any warnings
    GPIO.setmode(GPIO.BCM)  # Programming the GPIO by BCM pin number
    
    # Initialize GPIO Pins as Outputs
    GPIO.setup(13, GPIO.OUT) # A
    GPIO.setup(6, GPIO.OUT)  # B
    GPIO.setup(16, GPIO.OUT) # C
    GPIO.setup(20, GPIO.OUT) # D
    GPIO.setup(21, GPIO.OUT) # E
    GPIO.setup(19, GPIO.OUT) # F
    GPIO.setup(26, GPIO.OUT) # G

    # String of characters storing PORT values for each digit
      

# Assigning GPIO logic by taking 'pin' value
def PORT(pin):
    if(pin&0x01 == 0x01):
        GPIO.output(13,1)            # if  bit0 of 8bit 'pin' is true, pull PIN13 high
    else:
        GPIO.output(13,0)            # if  bit0 of 8bit 'pin' is false, pull PIN13 low
    if(pin&0x02 == 0x02):
        GPIO.output(6,1)             # if  bit1 of 8bit 'pin' is true, pull PIN6 high
    else:
        GPIO.output(6,0)            #if  bit1 of 8bit 'pin' is false, pull PIN6 low
    if(pin&0x04 == 0x04):
        GPIO.output(16,1)
    else:
        GPIO.output(16,0)
    if(pin&0x08 == 0x08):
        GPIO.output(20,1)
    else:
        GPIO.output(20,0)   
    if(pin&0x10 == 0x10):
        GPIO.output(21,1)
    else:
        GPIO.output(21,0)
    if(pin&0x20 == 0x20):
        GPIO.output(19,1)
    else:
        GPIO.output(19,0)
    if(pin&0x40 == 0x40):
        GPIO.output(26,1)
    else:
        GPIO.output(26,0)

# Assigning the conditions
def loop():
    dat = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F]
    while True:
        # For even numbers
        for x in range(10):
            if x % 2 == 0:
                pin = dat[x]
                PORT(pin);
                sleep(0.8)
        sleep(1.2)

        # For odd numbers
        for y in range(10):
            if y % 2 != 0:
                pin1 = dat[y]
                PORT(pin1);
                sleep(0.8)
        sleep(1.2)

        # For 0-9 numbers
        for z in range(10):
            pin2 = dat[z]
            PORT(pin2)
            sleep(0.8)
        sleep(1.2)

# To destroy/clean-up all the pins
def destroy():     
	GPIO.cleanup()              

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        print("Keyboard Interrupt Detected")
        destroy()
