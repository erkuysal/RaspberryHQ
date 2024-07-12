import time
import dht

# General usage imports
from machine import Pin


# Infrared Receiver imports
from ir_rx.nec import NEC_8
from ir_rx.print_error import print_error


# I2C 16x2 Led Screen's imports
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

# ------------------------- I2C SCREEN SETTINGS ------------------------------

# I2C Configurations
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

# Initialize I2C and LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# ------------------------ IR SETTINGS -------------------------------

irPin = 17
receiver = Pin(irPin, Pin.IN)

def callback(IRBit, param1, param2):
    print(IRBit)

IR = NEC_8(receiver, callback)

# -------------------------------------------------------

try:
    while True:
        pass
except KeyboardInterrupt:
    IR.close()
    print("Program Terminated")










