import time
import numpy as np
import adafruit_fxos8700
import adafruit_fxas21002c
import time
import os
import board
import busio

i2c = busio.I2C(board.SCL, board.SDA)
sensor1 = adafruit_fxos8700.FXOS8700(i2c) # accelerometer and magnetometer
sensor2 = adafruit_fxas21002c.FXAS21002C(i2c) # gyroscope


def setInitial(offset = [0,0,0]):
    #Sets the initial position for plotting and gyro calculations.
    print("Preparing to set initial angle. Please hold the IMU still.")
    time.sleep(3)
    print("Setting angle...")
    accelX, accelY, accelZ = sensor1.accelerometer #m/s^2
    magX, magY, magZ = sensor1.magnetometer #gauss
    #Calibrate magnetometer readings. Defaults to zero until you
    #write the code
    magX = magX - offset[0]
    magY = magY - offset[1]
    magZ = magZ - offset[2]
    roll = getRoll(accelX, accelY,accelZ)
    pitch = getPitch(accelX,accelY,accelZ)
    yaw = yaw_am(accelX,accelY,accelZ,magX,magY,magZ)
    print("Initial angle set.")
    return [roll,pitch,yaw]

def calibrateMag():
    #TODO: Set up lists, time, etc
    print("Preparing to calibrate magnetometer. Please wave around.")
    time.sleep(3)
    print("Calibrating...")
    #TODO: Calculate calibration constants
    magX_list = []
    magY_list = []
    magZ_list = []
<<<<<<< HEAD
    for i in range(8):
=======
    for i in range(500):
>>>>>>> cabfa118230a449c435725488b97e1d7a86b47d3
        magX, magY, magZ = sensor1.magnetometer
        magX_list.append(magX)
        magY_list.append(magY)
        magZ_list.append(magZ)
<<<<<<< HEAD
        time.sleep(1)
    return_list = [0,0,0]
    x = (min(magX_list)+max(magX_list))/2
    y = (min(magY_list)+max(magY_list))/2
    z = (min(magZ_list)+max(magZ_list))/2
=======
    return_list = [0,0,0]
    x = sum(magX_list)/500
    y = sum(magY_list)/500
    z = sum(magZ_list)/500
>>>>>>> cabfa118230a449c435725488b97e1d7a86b47d3
    return_list[0] = x
    return_list[1] = y
    return_list[2] = z
    print("Calibration complete.")
    return return_list

def calibrateGyro():
    #TODO
    print("Preparing to calibrate gyroscope. Put down the board and do not touch it.")
    time.sleep(3)
    print("Calibrating...")
    #TODO
    gyroX_list = []
    gyroY_list = []
    gyroZ_list = []
<<<<<<< HEAD
    for i in range(8):
=======
    for i in range(500):
>>>>>>> cabfa118230a449c435725488b97e1d7a86b47d3
        gyroX, gyroY, gyroZ = sensor2.gyroscope
        gyroX_list.append(gyroX)
        gyroY_list.append(gyroY)
        gyroZ_list.append(gyroZ)
<<<<<<< HEAD
        time.sleep(1)
    return_list = [0,0,0]
    x = (min(gyroX_list)+max(gyroX_list))/2
    y = (min(gyroY_list)+max(gyroY_list))/2
    z = (min(gyroZ_list)+max(gyroZ_list))/2
=======
    return_list = [0,0,0]
    x = sum(gyroX_list)/500
    y = sum(gyroY_list)/500
    z = sum(gyroZ_list)/500
>>>>>>> cabfa118230a449c435725488b97e1d7a86b47d3
    return_list[0] = x
    return_list[1] = y
    return_list[2] = z
    print("Calibration complete.")
    return return_list

if __name__ == "__main__":
    print(calibrateMag())
<<<<<<< HEAD
=======
    time.sleep(5)
>>>>>>> cabfa118230a449c435725488b97e1d7a86b47d3
    print(calibrateGyro())
