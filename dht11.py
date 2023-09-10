from dht import DHT11
from machine import Pin
from time import sleep

d = DHT11(Pin(4))

while True:
    d.measure()
    print(f"Temperature: {d.temperature()}{chr(176)}C, Humidity: {d.humidity()}%")
    sleep(2.)
    