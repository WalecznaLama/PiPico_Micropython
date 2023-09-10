import pcf8574
from machine import I2C, Pin
from utime import sleep

# Definicja pinów I2C
SDA_PIN = 0
SCL_PIN = 1

i2c = I2C(0, scl=Pin(SCL_PIN), sda=Pin(SDA_PIN))
pcf = pcf8574.PCF8574(i2c, 0x20)

# lepiej wyglada gdy na plytce stykowej led z P0 jest z lewej
def reverse_byte(b):
    result = 0
    for i in range(8):
        if b & (1 << i):
            result |= 1 << (7 - i)
    return result

while True:
    for value in range(256):  # 0x00 do 0xFF
        # Odwróć bity i zastosuj maskę 0xFF, aby wynik był 8-bitowy - dioda swieci na 0
        inverted_value = ~value & 0xFF  
        pcf.port = reverse_byte(inverted_value)
        sleep(0.3)