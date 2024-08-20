import sys
import time
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

right_thigh_id = 1
left_thigh_id = 0
right_feet_id = 2
left_feet_id = 3

right_armpit_id = 4

right_thigh_angle = 90
left_thigh_angle = 90
right_feet_angle = 90
left_feet_angle = 90

right_armpit_angle = 0

default_angle = {
right_thigh_id: right_thigh_angle,
left_thigh_id: left_thigh_angle,
right_feet_id: right_feet_angle,
left_feet_id: left_feet_angle,

right_armpit_id: right_armpit_angle
}

position = sys.argv[1]

def servo(id, angle):
  if id in default_angle.keys():
    kit.servo[id].angle = angle + default_angle[id]
  else:
    kit.servo[id].angle = angle

def stand_up():
  for id in default_angle.keys():
    print(id)
    servo(id, 0)

def left_leg_up(angle):
  servo(left_thigh_id, angle)
  servo(left_feet_id, angle)
  servo(right_armpit_id, angle)

def squat():
  servo(right_thigh_id, 60)
  servo(left_thigh_id, 60)
  servo(right_feet_id, -60)
  servo(left_feet_id, 60)

if position == 'stand':
  print('standing up')
  stand_up()

if position == 'squat':
  print('squating')
  squat()

if position == 'left-up':
  print('lifting left leg')
  angle = int(sys.argv[2])
  left_leg_up(angle)

if position == 'move':
  print('alternating between squat and stand')
  stand_up()
  time.sleep(1)
  squat()
  time.sleep(1)
  stand_up()
