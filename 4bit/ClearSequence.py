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

def send_to_lcd(binary_value):
    GPIO.output(RS, GPIO.LOW)
    GPIO.output(RW, GPIO.LOW)
    
    GPIO.output(DB7, GPIO.HIGH if binary_value[0] == '1' else GPIO.LOW)
    GPIO.output(DB6, GPIO.HIGH if binary_value[1] == '1' else GPIO.LOW)
    GPIO.output(DB5, GPIO.HIGH if binary_value[2] == '1' else GPIO.LOW)
    GPIO.output(DB4, GPIO.HIGH if binary_value[3] == '1' else GPIO.LOW)
    GPIO.output(E, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(E, GPIO.LOW)
    sleep(0.05)

    GPIO.output(DB7, GPIO.HIGH if binary_value[4] == '1' else GPIO.LOW)
    GPIO.output(DB6, GPIO.HIGH if binary_value[5] == '1' else GPIO.LOW)
    GPIO.output(DB5, GPIO.HIGH if binary_value[6] == '1' else GPIO.LOW)
    GPIO.output(DB4, GPIO.HIGH if binary_value[7] == '1' else GPIO.LOW)
    GPIO.output(E, GPIO.HIGH)
    sleep(0.05)
    GPIO.output(E, GPIO.LOW)
    sleep(0.05)

    print(binary_value[0])
    print(binary_value[1])
    print(binary_value[2])
    print(binary_value[3])
    print(binary_value[4])
    print(binary_value[5])
    print(binary_value[6])
    print(binary_value[7])
    print("------------")
    sleep(0.1)

send_to_lcd("00000001")

# Cleanup GPIO
GPIO.cleanup()
