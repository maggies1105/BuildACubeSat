import sys
from picamera import PiCamera
import os
import time
import threading
from imagingnew import *
from imu_new import *
from bluetooth import *


# set global variables
takenCount = 0
sentCount = 0
orbitNum = 1
targetAngle = 0
yawList = []
yaw = 0
lock = threading.Lock()
totalBytes = 0

# main orbit code that starts imaging threads and imu thread
def main():
    global targetAngle
    global yaw
    global yawList
    
    targetAngle = getYaw()+40
    print("target yaw:",(getYaw()+40))
    while True:
        yaw = getYaw()
        if abs(yaw - targetAngle) < 5:
            yaw = round(yaw)
            yawList.append(yaw)
            
            # if the angle matches our target angle, we start an imaging thread
            print("starting imaging thread at yaw:",yaw)
            imgThread = threading.Thread(target=imgProcess)
            imgThread.start()
            
            # sleep for  seconds until it has rotated past the 5 degree threshold so it doesn't take more pictures
            time.sleep(2)

# thread that takes, processes, and sends(or doesn't) the image
def imgProcess():
    global targetAngle
    global takenCount
    global sentCount
    global orbitNum
    global yawList
    global totalBytes

    # call takePic() to take the picture and save to 'filepath'
    takenCount += 1
    filepath = takePic(orbitNum,takenCount,yaw)
    totalBytes += os.path.getsize(filepath)
    targetAngle += 120
    i = takenCount%3-1
    # if there is guano, send the image
    if hasGuano(filepath):
        sentCount+=1
        print("sending image")
        lock.acquire()
        sendData(filepath)
        lock.release()
        yawList[i] = yaw
    else:
        # None type value in yaw list in telem packet means that image did not have guano
        yawList[i] = None

    # if we're at the end of an orbit, send telemetry packet and offset angle
    if takenCount % 3 == 0:
        print("sending telem")
        targetAngle += 40
        telem = "Images taken: " + str(takenCount) + "\nImages sent: " + str(sentCount) + "\nTotal bytes sent: " + str(totalBytes)
        telem += "\nOrbit number: " + str(orbitNum)
        telem += "\nYaw values: " + str(yawList) + "\n"
        telemFilePath = writeTelem(telem)
        sendData(telemFilePath)
        orbitNum += 1
        yawList = []

    if targetAngle >= 360:
        targetAngle = targetAngle%360

 

# writes telemetry packet
def writeTelem(infoStr):
    filepath = f"/home/pi/telem{orbitNum}.txt"
    file = open(filepath, 'w')
    file.write(infoStr)
    file.close()
    return filepath

if __name__ == '__main__':
    main()
