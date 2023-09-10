from machine import Pin, time_pulse_us
import time

SOUND_SPEED = 340  # Speed of sound in air in m/s
TRIG_PULSE_DURATION_US = 10  # Duration of trigger pulse in microseconds

def setup_sensor(trig_pin, echo_pin):
    """Configure the trigger and echo pins."""
    trig = Pin(trig_pin, Pin.OUT)
    echo = Pin(echo_pin, Pin.IN)
    return trig, echo

def measure_distance(trig, echo):
    """Send a trigger pulse and measure the echo pulse duration."""
    # Prepare the trigger pulse
    trig.value(0)
    time.sleep_us(5)

    # Send a 10 us trigger pulse
    trig.value(1)
    time.sleep_us(TRIG_PULSE_DURATION_US)
    trig.value(0)

    # Measure the duration of the echo pulse
    duration = time_pulse_us(echo, 1, 30000)

    # If we got a valid pulse, calculate the distance
    if duration != -1:
        distance = SOUND_SPEED * duration / 20000
        return distance
    else:
        return None

def main():
    trig, echo = setup_sensor(15, 14)

    while True:
        distance = measure_distance(trig, echo)
        if distance is not None:
            print(f"Distance: {distance} cm")
        else:
            print("Failed to read sensor")
        time.sleep_ms(500)

if __name__ == "__main__":
    main()
