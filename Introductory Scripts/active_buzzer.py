from machine import Pin, PWM
from time import sleep
active_buzzer = Pin(4, Pin.OUT)

def play_active(dur):
    active_buzzer.value(1)
    sleep(dur)
    active_buzzer.value(0)

while True:
    play_active(1)
    sleep(1)
# Connections:
# Connect active buzzer ground to ground on ESP32 and positive lead of active buzzer to the selected pin.