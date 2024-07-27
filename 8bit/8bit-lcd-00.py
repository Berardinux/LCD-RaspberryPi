import RPi.GPIO as GPIO
from time import sleep

# GPIO Pin configuration (BCM mode)
RS = 16  # Register Select pin
RW = 12  # Read/Write pin
E = 1    # Enable pin

# Data Pins (only DB4 to DB7 are used in 4-bit mode)
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

try:
  GPIO.output(RS, GPIO.HIGH)
  GPIO.output(RW, GPIO.LOW)
    
  GPIO.output(DB7, GPIO.LOW)
  GPIO.output(DB6, GPIO.HIGH)
  GPIO.output(DB5, GPIO.LOW)
  GPIO.output(DB4, GPIO.LOW)
  GPIO.output(DB3, GPIO.LOW)
  GPIO.output(DB2, GPIO.LOW)
  GPIO.output(DB1, GPIO.HIGH)
  GPIO.output(DB0, GPIO.LOW)

  GPIO.output(E, GPIO.HIGH)
  sleep(0.0005)
  GPIO.output(E, GPIO.LOW)
  sleep(0.0005)

  GPIO.cleanup()


except KeyboardInterrupt:
    print("Program interrupted. Cleaning up GPIO...")
    GPIO.cleanup()
