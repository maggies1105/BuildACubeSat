import os
import time
from git import Repo

btAddr = 'DC:A6:32:33:AB:0D' # change to your ground pi BT address
ch = '9'

def sendData(filepath):
    try:
        os.system("obexftp --bluetooth " + btAddr + " --channel " + ch + " --put " + filepath)
    except:
        print("Couldn't send data")

def receiveData():
    filepath = "/home/pi/CubePenguin/Maggie/GroundStation"
    try:
        print("receive mode started")
        os.system("sudo obexpushd -B -o " + filepath + " -n")
    except:
        print("Couldn't receive data")

def gitPush():
    repo = Repo("/home/pi/CubePenguin")
    origin = repo.remote("origin")
    
    while True:
        try:
            origin.pull()
            repo.git.add("--all")
            repo.index.commit("updated")
            origin.push()
            print("push successful")
            time.sleep(10)
        except:
            print("push unsuccessful")
            pass
        #print("git started")
        #filepath = "~/CubePenguin/Maggie/Images"
        #os.system("cd " + filepath)
        #os.system("git add .")
        #os.system('git commit -m \"uploaded new files ')
        #os.system('git pull')
        #os.system('git push origin master')
        #time.sleep(5)
