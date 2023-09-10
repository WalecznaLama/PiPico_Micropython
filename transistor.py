from machine import Pin
from time import sleep

# Ustawienie GP15 jako wyjście
base_pin = Pin(15, Pin.OUT)

while True:
    # Włącz diodę LED (poprzez podanie napięcia na bazę tranzystora)
    base_pin.value(1)
    sleep(1)  # Świeć przez 1 sekundę

    # Wyłącz diodę LED (poprzez odcięcie napięcia na bazie tranzystora)
    base_pin.value(0)
    sleep(1)  # Czekaj przez 1 sekundę