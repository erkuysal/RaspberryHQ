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

# Define the mapping
ir_command_map = {
        -1 : ' ',
        69 : '1',
        70 : '2',
        71 : '3',
        68 : '4',
        64 : '5',
        67 : '6',
        7  : '7',
        21 : '8',
        9  : '9',
        25 : '0',
        22 : '*',
        13 : '#',
        24 : 'UP',
        90 : 'RIGHT',
        8  : 'LEFT',
        82 : 'DOWN',
        28 : 'SELECT'
    }

def callback(IRBit, param1, param2):
    command = ir_command_map.get(IRBit, 'Unknown Command')
    print(f"IRBit: {IRBit} -> Command: {command}")
    process_command(command)

IR = NEC_8(receiver, callback)



# -------------------------------------------------------

current_index = 0
menu = ["Timer" , "Option 2", "Option 3"]


def display_menu():
    lcd.clear()
    lcd.putstr(menu[current_index])
    

def process_command(command):
    global current_index
    if command == 'UP':
        current_index = (current_index - 1) % len(menu)
    elif command == 'DOWN':
        current_index = (current_index + 1) % len(menu)
    elif command == 'SELECT':
        lcd.clear()
        lcd.putstr(f"Selected: {menu[current_index]}")
        time.sleep(2)  # Show selection for 2 seconds
    display_menu()


# ------------------------ MAIN LOOP -------------------------------

lcd.clear()
lcd.putstr('Welcome!')
time.sleep(2)
display_menu()

try:
    while True:
        pass
except KeyboardInterrupt:
    IR.close()
    print("Program Terminated")










