import RPi.GPIO as GPIO
from time import sleep

# GPIO Pin configuration (BCM mode)
RS = 16  # Register Select pin
RW = 12  # Read/Write pin
E = 1    # Enable pin

# Data Pins
DB0 = 7
DB1 = 8
DB2 = 25
DB3 = 24
DB4 = 23
DB5 = 18
DB6 = 15
DB7 = 14

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RS, GPIO.OUT)
GPIO.setup(RW, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(DB0, GPIO.OUT)
GPIO.setup(DB1, GPIO.OUT)
GPIO.setup(DB2, GPIO.OUT)
GPIO.setup(DB3, GPIO.OUT)
GPIO.setup(DB4, GPIO.OUT)
GPIO.setup(DB5, GPIO.OUT)
GPIO.setup(DB6, GPIO.OUT)
GPIO.setup(DB7, GPIO.OUT)

def pulse_enable():
    GPIO.output(E, GPIO.HIGH)
    sleep(0.0005)
    GPIO.output(E, GPIO.LOW)
    sleep(0.0005)

def send_to_lcd(binary_value, mode):
    # Set RS mode (0 for command, 1 for data)
    GPIO.output(RS, mode)
    # Always write mode
    GPIO.output(RW, GPIO.LOW)
    
    # Send all 8 bits to the corresponding data pins
    GPIO.output(DB7, GPIO.HIGH if binary_value[0] == '1' else GPIO.LOW)
    GPIO.output(DB6, GPIO.HIGH if binary_value[1] == '1' else GPIO.LOW)
    GPIO.output(DB5, GPIO.HIGH if binary_value[2] == '1' else GPIO.LOW)
    GPIO.output(DB4, GPIO.HIGH if binary_value[3] == '1' else GPIO.LOW)
    GPIO.output(DB3, GPIO.HIGH if binary_value[4] == '1' else GPIO.LOW)
    GPIO.output(DB2, GPIO.HIGH if binary_value[5] == '1' else GPIO.LOW)
    GPIO.output(DB1, GPIO.HIGH if binary_value[6] == '1' else GPIO.LOW)
    GPIO.output(DB0, GPIO.HIGH if binary_value[7] == '1' else GPIO.LOW)
    
    pulse_enable()

try: 
    send_to_lcd("01000010", GPIO.HIGH)
    sleep(0.005)
    GPIO.cleanup()

except KeyboardInterrupt:
    print("Program interrupted. Cleaning up GPIO...")
    GPIO.cleanup()
