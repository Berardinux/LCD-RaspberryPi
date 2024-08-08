import RPi.GPIO as GPIO
from time import sleep

RS = 16
RW = 12
E = 1

DB4 = 23
DB5 = 18
DB6 = 15
DB7 = 14

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
  send_nibble(byte[:4], mode)
  send_nibble(byte[4:], mode)

def initialize_lcd():
  GPIO.output(RS, GPIO.LOW)
  GPIO.output(RW, GPIO.LOW)

  send_nibble("0011", GPIO.LOW) # Function set (8-bit)
  sleep(0.005)
  send_nibble("0011", GPIO.LOW) # Function set (8-bit)
  sleep(0.005)
  send_nibble("0011", GPIO.LOW) # Function set (8-bit)
  sleep(0.005)
  send_nibble("0010", GPIO.LOW) # Function set (4-bit)
  sleep(0.005)

  send_byte("00101000", GPIO.LOW) # Function set: 4-bit, 2 lines, 5x8 dots
  sleep(0.005)
  send_byte("00001000", GPIO.LOW) # Display OFF
  sleep(0.005)
  send_byte("00000001", GPIO.LOW) # Display clear
  sleep(0.005)
  send_byte("00000110", GPIO.LOW) # Entry mode set
  sleep(0.005)
  send_byte("00001100", GPIO.LOW) # Display ON, Cursor OFF, Blink OFF
  sleep(0.005)

initialize_lcd()

GPIO.cleanup()