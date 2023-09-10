from machine import Pin
import utime

# Lista z pinami, do których podłączona jest klawiatura
rows = [Pin(i, Pin.IN, Pin.PULL_UP) for i in range(0, 4)]  # R1, R2, R3, R4
cols = [Pin(i, Pin.OUT) for i in range(4, 7)]  # C1, C2, C3

# Mapa klawiszy
keys = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['*', '0', '#']
]

def read_keypad():
    key = None
    for j in range(3):
        cols[j].value(0)
        for i in range(4):
            if rows[i].value() == 0:
                key = keys[i][j]
                while rows[i].value() == 0:  # Czekaj, aż przycisk zostanie zwolniony
                    pass
                utime.sleep_ms(20)  # Debounce delay
        cols[j].value(1)
        if key is not None:
            break
    return key

while True:
    key = read_keypad()
    if key is not None:
        print("Naciśnięto klawisz:", key)
    utime.sleep(0.1)
