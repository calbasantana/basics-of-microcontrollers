from machine import Pin, PWM
from time import sleep, time

servo = PWM(Pin(26), freq=50)
button = Pin(25, Pin.IN, Pin.PULL_UP)

def set_servo_angle(angle):
    duty = 40 + (angle / 80) * (105 - 40)
    servo.duty(int(duty))
    sleep(0.5)

while True:
    if button.value() == 0:
        set_servo_angle(30)
        while button.value() == 0:
            sleep(0.1)
        set_servo_angle(0)
    sleep(1)
