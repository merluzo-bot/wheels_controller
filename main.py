from machine import Pin, PWM, UART
from time import sleep

uart = UART(1, baudrate=115200, tx=Pin(4), rx=Pin(5))

class Motor:
    max_vel = 800
    def __init__(self, step:int, direction:int, enable:int):
        self.step_pin = Pin(step, Pin.OUT)
        self.step = PWM(self.step_pin)
        self.step.duty_u16(512)
        self.step.freq(100)

        self.dir = Pin(direction, Pin.OUT)

        self.enable = Pin(enable, Pin.OUT)
        self.enable.value(0)

    def set_motor(self, vel, direction):
        print(100 + int(vel*self.max_vel))
        print(direction)
        self.step.freq(100 + int(vel*self.max_vel))
        self.dir.value(not direction)


L_motor = Motor(21, 20, 22)
L_motor.dir.value(1)
R_motor = Motor(10, 11, 12)
R_motor.dir.value(0)

led = Pin(25, Pin.OUT)
btn = Pin(24, Pin.IN, Pin.PULL_UP)

val = False

def exec_message(message):
    print(message)

    if message[0] == "S":
        L_motor.enable.value(0)
        R_motor.enable.value(0)
        L_motor.set_motor(0, 0)
        R_motor.set_motor(0, 0)

    if message[0] == "R":
        direction = 0 if message[2] == "+" else 1
        vel = int(message[3:6])
        R_motor.enable.value(1)
        R_motor.set_motor(vel/255, direction)

    if message[0] == "L":
        direction = 1 if message[2] == "+" else 0
        vel = int(message[3:6])
        L_motor.enable.value(1)
        L_motor.set_motor(vel/255, direction)

    if message[0] == "A":
        direction = 1 if message[2] == "+" else 0
        vel = int(message[3:6])
        R_motor.enable.value(1)
        R_motor.set_motor(vel/255, not direction)
        L_motor.enable.value(1)
        L_motor.set_motor(vel/255, direction)

    if message[0] == "D":
        R = int(message[2:5])
        L = int(message[6:9])
        R_motor.enable.value(1)
        R_motor.set_motor(R/255, 0 if message[1] == "+" else 1)
        L_motor.enable.value(1)
        L_motor.set_motor(L/255, 1 if message[5] == "+" else 0)


message = ""
while True:
    if uart.any():
        char = uart.read().decode()
        if char == "_":
            pass
        elif char == "*":
            if message != "": exec_message(message)
            message = ""
        else:
            message += char

