from machine import Pin
import time

ir_sensor = Pin(14, Pin.IN)

while True:
    sensor_value = ir_sensor.value()
    
    if sensor_value == 0:
        print("Obstacle detected!")
    else:
        print("No obstacle detected")
    
    time.sleep(0.5)

# Connections:
# Connect OUT to the selected pin. Connect VCC pin to 3.3V and GND to GND on the ESP 32.