from machine import Pin, ADC
from time import sleep

sensor = ADC(Pin(34))
sensor.atten(ADC.ATTN_11DB)

while True:
    value = sensor.read()

    if value < 1000:
        quality = "Great"
    elif value < 2000:
        quality = "Good"
    elif value < 3000:
        quality = "Average"
    else:
        quality = "Poor"

    print(quality)
    
    sleep(1)


# Connections:
# Connect AD to the selected pin. Connect VCC pin to 3.3V and GND to GND on the ESP 32.