import sys
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

right_thigh_id = 1
left_thigh_id = 0
right_feet_id = 2
left_feet_id = 3

right_thigh_angle = 90
left_thigh_angle = 90
right_feet_angle = 80
left_feet_angle = 100

default_angle = {
right_thigh_id: right_thigh_angle,
left_thigh_id: left_thigh_angle,
right_feet_id: right_feet_angle,
left_feet_id: left_feet_angle
}

position = sys.argv[1]

def servo(id, angle):
  if id in default_angle.keys():
    kit.servo[id].angle = angle + default_angle[id]
  else:
    kit.servo[id].angle = angle

def stand_up():
  for id in default_angle.keys():
    servo(id, 0)

def squat():
  servo(right_thigh_id, 20)
  servo(left_thigh_id, 20)
  servo(right_feet_id, 20)
  servo(left_feet_id, -20)
if position == 'stand':
  print('standing up')
  stand_up()

if position == 'squat':
  print('squating')
  squat()
