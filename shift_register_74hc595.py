from machine import Pin
import utime

# Constants for PIN IDs
DATA_PIN_ID = 13
LATCH_PIN_ID = 15
CLOCK_PIN_ID = 14

# Set pins to output PIN objects
dataPIN = Pin(DATA_PIN_ID, Pin.OUT)
latchPIN = Pin(LATCH_PIN_ID, Pin.OUT)
clockPIN = Pin(CLOCK_PIN_ID, Pin.OUT)

def update_shift_register(input_bits, data, clock, latch):
    # Start data sending
    clock.value(0)
    latch.value(0)
    clock.value(1)
  
    # Load data in reverse order
    for bit in reversed(input_bits):
        clock.value(0)
        data.value(int(bit))
        clock.value(1)

    # Store data on register
    clock.value(0)
    latch.value(1)
    clock.value(1)

def increment_bit_string(bit_string):
    # Convert bit string to integer
    int_value = int(bit_string, 2)
    
    # Increment integer value (and wrap around when reaching 256)
    int_value = (int_value + 1) % 256
    
    # Convert back to bit string
    new_bit_string = bin(int_value)[2:]
    
    # Pad with zeros to make it 8 bits long
    while len(new_bit_string) < 8:
        new_bit_string = '0' + new_bit_string
    
    return new_bit_string

# Main loop
bit_string="00000000"
while True:
    update_shift_register(bit_string, dataPIN, clockPIN, latchPIN)
    bit_string = increment_bit_string(bit_string)
    utime.sleep(0.1)
