from machine import Pin, PWM
from time import sleep, ticks_ms
from math import sin, pi, fabs

pwmPin = 16
cwPin = 14 
acwPin = 15

# Zainicjalizuj piny raz na początku
pwm = PWM(Pin(pwmPin))
cw = Pin(cwPin, Pin.OUT)
acw = Pin(acwPin, Pin.OUT)

def motorMove(speed):
    if speed > 100: 
        speed = 100.
    elif speed < -100: 
        speed = -100.

    pwm.freq(50)
    pwm.duty_u16(int(fabs(speed)/100.*65536.))

    if speed < 0:
        cw.value(0)
        acw.value(1)
    elif speed == 0:
        cw.value(0)
        acw.value(0)
    else:  # speed > 0
        cw.value(1)
        acw.value(0)

# main program
angle = 0.

while True:
    angle += .01
    if angle > 2*pi:
        angle = 0.

    speed = sin(angle) * 100.  # Wyliczamy prędkość na podstawie sinusa
    print(speed)

    motorMove(speed)
    sleep(0.02)
