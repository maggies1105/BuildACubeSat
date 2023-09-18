import threading
import time
from bluetooth import *

def main():
    receiveThread = threading.Thread(target=receiveData)
    pushThread = threading.Thread(target=gitPush)
    receiveThread.start()
    time.sleep(0.5)
    pushThread.start()

if __name__ == '__main__':
    main()

