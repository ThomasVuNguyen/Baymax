import sys
from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

id = sys.argv[1]
angle = sys.argv[2]
kit.servo[int(id)].angle = int(angle)
