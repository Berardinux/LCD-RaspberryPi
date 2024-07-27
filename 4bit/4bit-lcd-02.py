import RPi.GPIO as GPIO
from time import sleep

# GPIO Pin configuration (BCM mode)
RS = 16  # Register Select pin
RW = 12  # Read/Write pin
E = 1    # Enable pin

# Data Pins (only DB4 to DB7 are used in 4-bit mode)
DB4 = 23
DB5 = 18
DB6 = 15
DB7 = 14

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(RS, GPIO.OUT)
GPIO.setup(RW, GPIO.OUT)
GPIO.setup(E, GPIO.OUT)
GPIO.setup(DB4, GPIO.OUT)
GPIO.setup(DB5, GPIO.OUT)
GPIO.setup(DB6, GPIO.OUT)
GPIO.setup(DB7, GPIO.OUT)

def pulse_enable():
    GPIO.output(E, GPIO.HIGH)
    sleep(0.0005)
    GPIO.output(E, GPIO.LOW)
    sleep(0.0005)

def send_nibble(nibble, mode):
    GPIO.output(RS, mode)
    GPIO.output(RW, GPIO.LOW)
    
    GPIO.output(DB7, GPIO.HIGH if nibble[0] == '1' else GPIO.LOW)
    GPIO.output(DB6, GPIO.HIGH if nibble[1] == '1' else GPIO.LOW)
    GPIO.output(DB5, GPIO.HIGH if nibble[2] == '1' else GPIO.LOW)
    GPIO.output(DB4, GPIO.HIGH if nibble[3] == '1' else GPIO.LOW)
    
    pulse_enable()

def send_byte(byte, mode):
    send_nibble(byte[:4], mode)  # Send high nibble
    send_nibble(byte[4:], mode)  # Send low nibble

def letter_to_binary(letter):
    # Get ASCII value of the letter
    ascii_value = ord(letter)
    # Convert ASCII value to binary string and remove '0b' prefix
    binary_value = bin(ascii_value)[2:]
    # Ensure the binary string has 8 bits by padding with leading zeros
    binary_value = binary_value.zfill(8)
    return binary_value

def letter_to_lcd(letter):
    binary_representation = letter_to_binary(letter)
    send_byte(binary_representation, GPIO.HIGH)

# Initialize the LCD in 4-bit mode
def initialize_lcd():
    GPIO.output(RS, GPIO.LOW)
    GPIO.output(RW, GPIO.LOW)
    
    # Initialization sequence for 4-bit mode
    send_nibble("0011", GPIO.LOW)  # Function set (8-bit)
    sleep(0.005)
    send_nibble("0011", GPIO.LOW)  # Function set (8-bit)
    sleep(0.005)
    send_nibble("0011", GPIO.LOW)  # Function set (8-bit)
    sleep(0.005)
    send_nibble("0010", GPIO.LOW)  # Function set (4-bit)
    sleep(0.005)
    
    send_byte("00101000", GPIO.LOW)  # Function set: 4-bit, 2 lines, 5x8 dots
    sleep(0.005)
    send_byte("00001000", GPIO.LOW)  # Display OFF
    sleep(0.005)
    send_byte("00000001", GPIO.LOW)  # Display clear
    sleep(0.005)
    send_byte("00000110", GPIO.LOW)  # Entry mode set
    sleep(0.005)
    send_byte("00001100", GPIO.LOW)  # Display ON, Cursor OFF, Blink OFF
    sleep(0.005)

# Example usage
initialize_lcd()

try:
    # Display the string "Berardinux"
    for char in "Berardinux":
        letter_to_lcd(char)

except KeyboardInterrupt:
    print("Program interrupted. Cleaning up GPIO...")
    GPIO.cleanup()
