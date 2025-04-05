from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.show()

oled.text('Hello, ESP32!', 0, 0)
oled.text('OLED Display', 0, 20)
oled.text('MicroPython', 0, 40)
oled.show()

# Connections:
# Connect VCC and GND on OLED screen to 3.3V and GND on ESP32, respectively.
# Connect SCL and SDA to selected pins on ESP32.