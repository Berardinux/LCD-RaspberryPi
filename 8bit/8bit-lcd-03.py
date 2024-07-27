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
    send_to_lcd(binary_representation, GPIO.HIGH)

# Initialize the LCD in 8-bit mode
def initialize_lcd():
    GPIO.output(RS, GPIO.LOW)
    GPIO.output(RW, GPIO.LOW)
    
    # Initialization sequence
    send_to_lcd("00110000", GPIO.LOW)  # Function set: 8-bit
    sleep(0.005)
    send_to_lcd("00110000", GPIO.LOW)  # Function set: 8-bit
    sleep(0.005)
    send_to_lcd("00110000", GPIO.LOW)  # Function set: 8-bit
    sleep(0.005)
    send_to_lcd("00111000", GPIO.LOW)  # Function set: 8-bit, 2 lines, 5x8 dots
    sleep(0.005)

    send_to_lcd("00001000", GPIO.LOW)  # Display OFF
    sleep(0.005)
    send_to_lcd("00000001", GPIO.LOW)  # Display clear
    sleep(0.005)
    send_to_lcd("00000110", GPIO.LOW)  # Entry mode set
    sleep(0.005)
    send_to_lcd("00001100", GPIO.LOW)  # Display ON, Cursor OFF, Blink OFF
    sleep(0.005)

# Example usage
initialize_lcd()

try: 
    # Display the string "Berardinux"
    while True:
        for char in "   Berardinux   ++++++++++++++++++++++++    Is Cool!":
            letter_to_lcd(char)
        sleep(2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)
        
        for char in "* Hello World! *++++++++++++++++++++++++* Hello World! *":
            letter_to_lcd(char)
        sleep(2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in ">               ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "->              ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "-->             ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "--->            ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "---->           ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----->          ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "------>         ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "------->        ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "-------->       ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "--------->      ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "---------->     ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------->    ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "------------>   ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "------------->  ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "--------------> ++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "--------------->++++++++++++++++++++++++":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++>":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++-->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++--->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++---->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++----->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++------>":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++------->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++-------->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++--------->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++---------->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++----------->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++------------>":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++------------->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++-------------->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "----------------++++++++++++++++++++++++--------------->":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

        for char in "################++++++++++++++++++++++++################>":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.2)

        for char in "################++++++++++++++++++++++++################>":
            letter_to_lcd(char)
        sleep(.2)
        send_to_lcd("00000001", GPIO.LOW)  # Display clear
        sleep(.005)

except KeyboardInterrupt:
    print("Program interrupted. Cleaning up GPIO...")
    GPIO.cleanup()
