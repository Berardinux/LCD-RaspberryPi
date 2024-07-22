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
    # Send each bit to corresponding data pin
    GPIO.output(DB7, GPIO.HIGH if binary_value[0] == '1' else GPIO.LOW)
    GPIO.output(DB6, GPIO.HIGH if binary_value[1] == '1' else GPIO.LOW)
    GPIO.output(DB5, GPIO.HIGH if binary_value[2] == '1' else GPIO.LOW)
    GPIO.output(DB4, GPIO.HIGH if binary_value[3] == '1' else GPIO.LOW)
    GPIO.output(DB3, GPIO.HIGH if binary_value[4] == '1' else GPIO.LOW)
    GPIO.output(DB2, GPIO.HIGH if binary_value[5] == '1' else GPIO.LOW)
    GPIO.output(DB1, GPIO.HIGH if binary_value[6] == '1' else GPIO.LOW)
    GPIO.output(DB0, GPIO.HIGH if binary_value[7] == '1' else GPIO.LOW)

    # Pulse the enable pin
    GPIO.output(E, GPIO.HIGH)
    sleep(0.001)
    GPIO.output(E, GPIO.LOW)
    sleep(0.001)

def init_lcd():
    # Set to 8-bit mode
    GPIO.output(RS, GPIO.LOW)
    GPIO.output(RW, GPIO.LOW)

    # Function set: 8-bit, 2 lines, 5x8 dots
    send_to_lcd("00111000")

    # Display on, cursor off, blink off
    send_to_lcd("00001100")

    # Clear display
    send_to_lcd("00000001")
    sleep(0.002)  # Clear command needs more time

    # Entry mode set: increment cursor, no shift
    send_to_lcd("00000110")

def write_char(char):
    # Set RS for data
    GPIO.output(RS, GPIO.HIGH)
    GPIO.output(RW, GPIO.LOW)

    # Send character to LCD
    send_to_lcd(f"{ord(char):08b}")

# Main program
init_lcd()
write_char('H')

# Cleanup GPIO
GPIO.cleanup()
