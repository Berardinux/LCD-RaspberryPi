import RPi.GPIO as GPIO
from time import sleep

# GPIO Pin configuration (BCM mode)
RS = 16  # Register Select pin
RW = 12  # Read/Write pin
E = 1    # Enable pin
DATA_PINS = [7, 8, 25, 24, 23, 18, 15, 14]  # DB0 to DB7

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RS, GPIO.OUT)
GPIO.setup(RW, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
for pin in DATA_PINS:
    GPIO.setup(pin, GPIO.OUT)

def pulse_enable():
    GPIO.output(E, True)
    sleep(0.0005)
    GPIO.output(E, False)
    sleep(0.0005)

def send_nibble(data):
    for i in range(4):
        GPIO.output(DATA_PINS[i+4], data & (1 << i))  # Use higher nibble
    pulse_enable()

def send_byte(data, char_mode=False):
    GPIO.output(RS, char_mode)
    GPIO.output(RW, False)  # Ensure write mode
    send_nibble(data >> 4)  # Send high nibble
    send_nibble(data & 0x0F)  # Send low nibble

def init_lcd():
    # Initialize display
    send_byte(0x33)  # Initialization
    send_byte(0x32)  # Initialization
    send_byte(0x28)  # 2 line, 5x7 matrix
    send_byte(0x0C)  # Display on, cursor off, blink off
    send_byte(0x06)  # Increment cursor
    send_byte(0x01)  # Clear display
    sleep(0.005)  # Delay for clear display

def write_char(char):
    send_byte(ord(char), True)

# Main program
init_lcd()
write_char('A')

sleep(10)

# Cleanup GPIO
GPIO.cleanup()

