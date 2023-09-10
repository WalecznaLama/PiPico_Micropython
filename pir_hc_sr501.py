from machine import Pin
import time

def setup_sensor(pir_pin):
    """Configure the PIR sensor pin."""
    pir = Pin(pir_pin, Pin.IN, Pin.PULL_DOWN)
    return pir

def detect_motion(pir):
    """Detect motion using the PIR sensor."""
    if pir.value() == 1:
        return True
    else:
        return False

def main():
    pir = setup_sensor(0)
    motion_counter = 0

    print('Starting up the PIR Module')
    time.sleep(1)
    print('Ready')

    while True:
        if detect_motion(pir):
            motion_counter += 1
            print(f'Motion Detected {motion_counter}')
        time.sleep(1)

if __name__ == "__main__":
    main()
