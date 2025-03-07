from machine import Pin, PWM
from time import sleep, time

servo = PWM(Pin(26), freq=50)
button = Pin(25, Pin.IN, Pin.PULL_UP)

def set_servo_angle(angle):
    duty = 40 + (angle / 80) * (105 - 40)
    servo.duty(int(duty))
    sleep(0.5)

last_open_time = 0
def daily_open():
    global last_open_time
    if time() - last_open_time >= 86400:
        last_open_time = time()
        set_servo_angle(30)
        sleep(3)
        set_servo_angle(0)

while True:
    daily_open()
    if button.value() == 0:
        set_servo_angle(30)
        while button.value() == 0:
            sleep(0.1)
        set_servo_angle(0)
    sleep(1)
