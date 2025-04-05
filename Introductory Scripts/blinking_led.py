from machine import Pin
from time import sleep
led = Pin(13, Pin.OUT)
while True:
    led.on()
    sleep(0.5)
    led.off()
    sleep(0.5)

# Connections:
# Connect Resistor between LED positive lead (longer one) and the selected pin.
# Connect the LED negative lead (shorter one) to ground on ESP32.
