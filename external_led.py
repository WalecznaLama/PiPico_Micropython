from machine import Pin, Timer, PWM, ADC
import time

# # Just blinking LED
# led = Pin(15, Pin.OUT)
# timer = Timer()
# 
# def blink(timer):
#     led.toggle()
# 
# timer.init(freq=0.2, mode=Timer.PERIODIC, callback=blink)

# # Button toggle
# led = Pin(15, Pin.OUT)
# button = Pin(14, Pin.IN, Pin.PULL_DOWN)
# 
# while True:
#     if button.value():
#         led.toggle()
#         time.sleep(0.5)

# # PWM brightness
# pwm = PWM(Pin(15))
# 
# pwm.freq(1000)
# 
# while True:
#     for duty in range(65025):
#         pwm.duty_u16(duty)
#         time.sleep(0.0002)
#     for duty in range(65025, 0, -1):
#         pwm.duty_u16(duty)
#         time.sleep(0.0002)

# ADC brightness

pwm = PWM(Pin(15))
adc = ADC(Pin(26))

pwm.freq(1000)

while True:
    duty = adc.read_u16()
    pwm.duty_u16(duty)