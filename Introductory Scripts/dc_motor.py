from machine import Pin, PWM
from time import sleep

motor_a_in1 = PWM(Pin(34), freq=1000)
motor_a_in2 = PWM(Pin(35), freq=1000)

def motor_a_forward(speed=300):
    motor_a_in1.duty(speed)
    motor_a_in2.duty(0)

def motor_a_backward(speed=300):
    motor_a_in1.duty(0)
    motor_a_in2.duty(speed)

def motor_a_stop():
    motor_a_in1.duty(0)
    motor_a_in2.duty(0)

motor_a_forward(300)
sleep(2)
motor_a_backward(300)
sleep(2)
motor_a_stop()

# Connections:
# Connect pins on the motor driver to the selected pins on the ESP32.
# Connect the motor driver to external power (3V or 6V).