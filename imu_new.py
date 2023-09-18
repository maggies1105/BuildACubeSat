import numpy as np
import adafruit_fxos8700
import adafruit_fxas21002c
import time
import board
import busio
import math
# from calibration import *

# initialize sensor1 and sensor2
i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_fxos8700.FXOS8700(i2c) # accelerometer and magnetometer
sensor2 = adafruit_fxas21002c.FXAS21002C(i2c) # gyroscope

yaw0 = 30

def getOrientation():
    accelX, accelY, accelZ = sensor1.accelerometer
    roll = math.atan2(accelY, math.sqrt(accelX**2 + accelZ**2))
    pitch = math.atan2(accelX, math.sqrt(accelY**2 + accelZ**2))
    return [pitch, roll]

def getRoll():
    accelX, accelY, accelZ = sensor1.accelerometer
    return math.atan2(accelY, math.sqrt(accelX**2 + accelZ**2))

def getPitch():
    accelX, accelY, accelZ = sensor1.accelerometer
    return math.atan2(accelX, math.sqrt(accelY**2 + accelZ**2))

def getYaw():
    magX, magY, magZ = sensor1.magnetometer  # gauss
    # magOffset = [7.699999999999999, -36.85, -60.2]
    # magOffset = [28.19259999999997, -22.323199999999982, -52.963200000000164]
    magOffset = [16.155599999999986, -27.290000000000006, -79.56939999999994]
    # magOffset = [12.0, -37.55, -55.45]
    # magScale = [0.9468449931412894, 1.0446462353386303, 1.013582966226138]
    magScale = [1,1,1]
    magX = (magX - magOffset[0]) * magScale[0]
    magY = (magY - magOffset[1]) * magScale[1]
    magZ = (magZ - magOffset[2]) * magScale[2]
    magY = -magY
    magZ = -magZ
    # pitch = getPitch() # roll = getRoll()
    pitch, roll = getOrientation()
    Xh = magX*math.cos(pitch) + magY*math.sin(pitch)*math.sin(roll) + magZ*math.cos(roll)*math.sin(pitch)
    Yh = magY*math.cos(roll) - magZ*math.sin(roll)
    yaw = 180 - math.degrees(math.atan2(-Yh,Xh))
    #if yaw < 0: yaw += 360
    #return (360-yaw)
    return yaw


if __name__ == '__main__':
    count = 1
    while True:
        print(count,".",getYaw())
        count += 1
        time.sleep(0.1)
