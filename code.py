import time
import board
import pulseio
from adafruit_motor import servo
import simpleio

import adafruit_hcsr04
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D2, echo_pin=board.D7)

#declaring pwm for each servo
pwm9 = pulseio.PWMOut(board.D9, duty_cycle=2 ** 15, frequency=50)
time.sleep(0.1)
pwm3 = pulseio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
time.sleep(0.1)
pwm5 = pulseio.PWMOut(board.D5, duty_cycle=2 ** 15, frequency=50)
time.sleep(0.1)
pwm4 = pulseio.PWMOut(board.D4, duty_cycle=2 ** 15, frequency=50)
time.sleep(0.1)
pwm6 = pulseio.PWMOut(board.D6, duty_cycle=2 ** 15, frequency=50)
time.sleep(0.1)
pwm8 = pulseio.PWMOut(board.D8, duty_cycle=2 ** 15, frequency=50)
time.sleep(0.1)
pwm11 = pulseio.PWMOut(board.D11, duty_cycle=2 ** 15, frequency=50)
time.sleep(0.1)
pwm12 = pulseio.PWMOut(board.D12, duty_cycle=2 ** 15, frequency=50)
time.sleep(0.1)

#creating servo objects for each servo
right_rear_top = servo.Servo(pwm3)
right_rear_bot = servo.Servo(pwm4)
right_front_top = servo.Servo(pwm6)
right_front_bot = servo.Servo(pwm5)
left_rear_top = servo.Servo(pwm11)
left_rear_bot = servo.Servo(pwm12)
left_front_top = servo.Servo(pwm8)
left_front_bot = servo.Servo(pwm9)

#standard leg orientation functions
def default_left_front(temp_top,temp_bot):
    temp_top.angle = 140
    temp_bot.angle = 60
def default_left_rear(temp_top,temp_bot):
    temp_top.angle = 130
    temp_bot.angle = 90
def default_right_rear(temp_top,temp_bot):
    temp_top.angle = 35
    temp_bot.angle = 110
def default_right_front(temp_top,temp_bot):
    temp_top.angle = 40
    temp_bot.angle = 100

#walking
def walk(left_front_top,left_front_bot,left_rear_top,left_rear_bot,right_front_top,right_front_bot,right_rear_top,right_rear_bot):
    print("walking")

    #moving leading with left leg--------------------------------------------------
    #loop for moving all top joints---------
    for angle in range(140, 90, -5):
        #incrementing right rear top
        left_front_top.angle = angle
        time.sleep(0.01)
    for angle2 in range(35, 60, 5):  # 0 - 180 degrees, 5 degrees at a time.
        right_rear_top.angle = angle2
        time.sleep(0.01)
    for angle3 in range(40,0,-5):
        right_front_top.angle = angle3
        time.sleep(0.01)
    for angle4 in range(130,180,5):
        left_rear_top.angle = angle4
        time.sleep(0.01)
    #loop for moving all bot joints---------
    for angle in range(60,10,-5):
        left_front_bot.angle = angle
        time.sleep(0.01)
    for angle2 in range(110, 70, -5):  # 0 - 180 degrees, 5 degrees at a time.
        right_rear_bot.angle = angle2
        time.sleep(0.01)
    for angle3 in range(100,120,5):
        right_front_bot.angle = angle3
        time.sleep(0.01)
    for angle4 in range(90,80,-5):
        left_rear_bot.angle = angle4
        time.sleep(0.01)
    time.sleep(0.5)

    #moving transition to right leg---------------------------------------------

    for angle3 in range(0,140,5):
        right_front_top.angle = angle3
        time.sleep(0.01)
    for angle4 in range(180,120,-5):
        left_rear_top.angle = angle4
        time.sleep(0.01)
    for angle2 in range(60, 0, -5):  # 0 - 180 degrees, 5 degrees at a time.
        right_rear_top.angle = angle2
        time.sleep(0.01)
    for angle in range(90, 155, 5):
        #incrementing right rear top
        left_front_top.angle = angle
        time.sleep(0.01)

    #loop for moving all bot joints---------
    for angle3 in range(120,140,5):
        right_front_bot.angle = angle3
        time.sleep(0.01)
    for angle4 in range(80,60,-5):
        left_rear_bot.angle = angle4
        time.sleep(0.01)
    for angle2 in range(70, 110, 5):  # 0 - 180 degrees, 5 degrees at a time.
        right_rear_bot.angle = angle2
        time.sleep(0.01)
    for angle in range(10,70,5):
        left_front_bot.angle = angle
        time.sleep(0.01)
    time.sleep(0.5)

#Robot operations
print("start servos")
default_left_front(left_front_top,left_front_bot)
time.sleep(0.1)
default_right_rear(right_rear_top,right_rear_bot)
time.sleep(0.1)
default_left_rear(left_rear_top,left_rear_bot)
time.sleep(0.1)
default_right_front(right_front_top,right_front_bot)
print("Starting walk")
time.sleep(2)

#walk(left_front_top,left_front_bot,left_rear_top,left_rear_bot,right_front_top,right_front_bot,right_rear_top,right_rear_bot)
#walk(left_front_top,left_front_bot,left_rear_top,left_rear_bot,right_front_top,right_front_bot,right_rear_top,right_rear_bot)
#walk(left_front_top,left_front_bot,left_rear_top,left_rear_bot,right_front_top,right_front_bot,right_rear_top,right_rear_bot)

while sonar.distance > 8:
    walk(left_front_top,left_front_bot,left_rear_top,left_rear_bot,right_front_top,right_front_bot,right_rear_top,right_rear_bot)
    if sonar.distance <= 8:
        default_left_front(left_front_top,left_front_bot)
        time.sleep(0.1)
        default_right_rear(right_rear_top,right_rear_bot)
        time.sleep(0.1)
        default_left_rear(left_rear_top,left_rear_bot)
        time.sleep(0.1)
        default_right_front(right_front_top,right_front_bot)
        time.sleep(3)