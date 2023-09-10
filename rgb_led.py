from machine import Pin, PWM
from time import sleep

PWM_FREQ = 1000
U16_DUTY_MAX = 65025
LOOP_STEP = 100
SLEEP_TIME = 0.001

# Ustaw piny dla kolorów RGB
pin_r = PWM(Pin(2))  # Pin dla czerwonego koloru
pin_g = PWM(Pin(3))  # Pin dla zielonego koloru
pin_b = PWM(Pin(4))  # Pin dla niebieskiego koloru

# Ustaw częstotliwość PWM
pin_r.freq(PWM_FREQ)
pin_g.freq(PWM_FREQ)
pin_b.freq(PWM_FREQ)

# Ustaw początkową jasność na 0 (wspólna anoda w LED)
pin_r.duty_u16(U16_DUTY_MAX)
pin_g.duty_u16(U16_DUTY_MAX)
pin_b.duty_u16(U16_DUTY_MAX)

def change_color(pin: PWM):
    for duty in range(U16_DUTY_MAX, 0, -LOOP_STEP):
        pin.duty_u16(duty)
        sleep(SLEEP_TIME)
    for duty in range(0, U16_DUTY_MAX, LOOP_STEP):
        pin.duty_u16(duty)
        sleep(SLEEP_TIME)

while True:
    # Czerwony
    change_color(pin_r)

    # Zielony
    change_color(pin_g)

    # Niebieski
    change_color(pin_b)