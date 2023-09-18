import cv2
import time
import numpy as np
from picamera import PiCamera
import time
from datetime import datetime

# setup pi camera
camera = PiCamera()
camera.resolution = (656, 493)

now = datetime.now()

# takes picture
def takePic(orbitNum, takenNum, yaw):
    imgNum = 3 if takenNum%3==0 else takenNum%3
    # '2_3_36' would be the 3rd image taken in orbit #2 at 36 deg
    filepath = ('/home/pi/Pictures/%s%s%s%s%s.jpg' % (str(orbitNum), '_', str(imgNum), '_', str(yaw)))  # placeholder folder, we should add a new one for images
    print("taking picture")
    camera.capture(filepath)
    return filepath

# returns True if there is guano present
def hasGuano(filepath):
    image = cv2.imread(filepath)
    '''red_range = [(0, 0, 100), (100, 100, 255)]
    red = cv2.inRange(image, red_range[0], red_range[1])'''
    image_hsv = cv2.fastNlMeansDenoisingColored(image, None, 3, 3, 7, 21)
    hsv_image = cv2.cvtColor(image_hsv, cv2.COLOR_BGR2HSV)  # Converts BGR image to HSV format
    hsv_range = [(0, 50, 50), (15, 255, 255)]
    red = cv2.inRange(hsv_image, hsv_range[0], hsv_range[1])
    red_count = np.count_nonzero(red == 255)
    total_pixels = image.shape[0] * image.shape[1]
    perc_red = red_count / total_pixels
    area = round(71733.51 * perc_red)
    if area > 200:
        return True
    return False

# can be used to check mask -- not necessarily necessary for final project code
def get_mask(image, lower_bound, upper_bound):
    threshold = cv2.inRange(image, lower_bound, upper_bound)
    mask = cv2.bitwise_and(image, image, mask=threshold)
    path = '/home/pi/CubePenguin/Maggie/Images'
    cv2.imwrite(path, mask)

