from machine import ADC, Pin
from time import sleep

# Definiowanie stałych
PHOTO_PIN_NUMBER = 26
ADC_MAX_VALUE = 65535

def read_light_percentage(photo_pin_number):
    """
    Czyta wartość z fotorezystora podłączonego do podanego pinu
    i zwraca jasność jako procent maksymalnej wartości.
    """
    photo_resistor = ADC(Pin(photo_pin_number))
    light_value = photo_resistor.read_u16()
    light_percentage = round(light_value / ADC_MAX_VALUE * 100, 2)
    return light_percentage

while True:
    print(f"Light: {read_light_percentage(PHOTO_PIN_NUMBER)}%")
    sleep(0.33)
