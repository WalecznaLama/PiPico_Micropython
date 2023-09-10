from machine import I2C, Pin
from time import sleep
from i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
while True:
    lcd.clear()
    sleep(0.5)
    heart = bytearray([0x00,0x0a,0x1f,0x1f,0x0e,0x04,0x00,0x00])
    smile = bytearray([0x0, 0x1b, 0x1b, 0x0, 0x11, 0x1b, 0xa, 0x4])
    lcd.custom_char(0, heart)
    lcd.custom_char(1, smile)
    lcd.putstr("Hello World!\n"+chr(0)+" <special> "+chr(1))
    
    sleep(2)
    lcd.clear()
    for i in range(15):
        lcd.move_to(i, i%2)
        lcd.putchar(str(i%10))
        sleep(0.4)
        lcd.clear()