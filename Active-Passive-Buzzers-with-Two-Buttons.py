from machine import Pin, PWM
from time import sleep

passive_buzzer = Pin(4, Pin.OUT)
active_buzzer = Pin(5, Pin.OUT)
button1 = Pin(18, Pin.IN, Pin.PULL_UP)
button2 = Pin(19, Pin.IN, Pin.PULL_UP)

def play_passive_buzzer(frequency, duration):
    pwm = PWM(passive_buzzer, freq=frequency, duty=512)
    sleep(duration)
    pwm.deinit()

def play_active_buzzer(duration):
    active_buzzer.value(1)
    sleep(duration)
    active_buzzer.value(0)

while True:
    if button1.value() == 0:
        play_passive_buzzer(1000, 1)
        sleep(0.1)
    
    if button2.value() == 0:
        play_active_buzzer(1)
        sleep(0.1)
