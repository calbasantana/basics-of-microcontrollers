import utime
from machine import Pin, I2C

import ahtx0

i2c = I2C(scl=Pin(22), sda=Pin(21))

sensor = ahtx0.AHT10(i2c)

while True:
    print("\nTemperature: %0.2f C" % sensor.temperature)
    print("Humidity: %0.2f %%" % sensor.relative_humidity)
    utime.sleep(5)

# Connections:
# Connect sensor pins to selected pins on the ESP32.
# Connect VCC and GND from sensor to 3.3V and GND on the ESP32, respectively.