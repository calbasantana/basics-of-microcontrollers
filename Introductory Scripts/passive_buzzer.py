from machine import Pin
from time import sleep

buzzer = Pin(4, Pin.OUT)

while True:
    buzzer.value(1)  
    sleep(1)  
    buzzer.value(0)
    sleep(1)

# Connections:
# Connect passive buzzer ground to ground on ESP32 and positive lead of passive buzzer to the selected pin.
