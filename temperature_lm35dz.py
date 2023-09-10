from machine import ADC

def adc_to_voltage(adc_value):
    """Convert ADC reading to voltage."""
    max_adc_value = 65535
    reference_voltage = 3.3
    voltage = (adc_value / max_adc_value) * reference_voltage
    return voltage

def voltage_to_temperature(voltage):
    """Convert voltage to temperature for LM35DZ."""
    return voltage / 0.01


def fahrenheit(celsius):
    return (celsius * (9/5)) + 32


adc = ADC(28)

reading = adc.read_u16()
voltage = adc_to_voltage(reading)
celsius_temp = voltage_to_temperature(voltage)

fahrenheit_temp = fahrenheit(celsius_temp)

print("Reading {}\nCelsius {}\nFahrenheit {}".format(
    reading, celsius_temp, fahrenheit_temp))