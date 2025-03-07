from machine import Pin
import time

led_pin = Pin(5, Pin.OUT)
button_pin = Pin(18, Pin.IN, Pin.PULL_UP)

while True:
    if button_pin.value() == 0:
        led_pin.value(1)
    else:
        led_pin.value(0)
    time.sleep(0.1)
