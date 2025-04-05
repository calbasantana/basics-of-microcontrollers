from machine import Pin
import time

ldr_d0 = Pin(34, Pin.IN)


led = Pin(2, Pin.OUT)

while True:
    light_level = ldr_d0.value()
    print("LDR Digital Value:", light_level)
    
    if light_level == 0:
        led.on()
    else:
        led.off()

    time.sleep(1)

# Connections:
# Connect VCC and GND on LDR to 3.3V and GND on ESP32, respectively. Connect D0 to selected pin on ESP32.
# Connect the LED negative lead (shorter one) to ground on ESP32.
# Connect Resistor between LED positive lead (longer one) and the selected pin.
