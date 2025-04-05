from machine import Pin, PWM
from time import sleep
servo = PWM(Pin(23), freq=50)
def set_angle(angle):
    servo.duty(int(40 + (angle / 180) * 65))

while True:
    set_angle(0)
    sleep(2)
    set_angle(70)
    sleep(2)

# Connections:
# Connect the data pin of the servo to the selected pin.
# Connect the ground pin (brown) of the servo to ground on the ESP32 and the positive lead (red) to 3V3 on the ESP32.