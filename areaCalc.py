import cv2
import numpy as np

def main(filepath):
    #area = (bgr(filepath) + hsv(filepath))/2
    print("area:",bgr(filepath),"mm^2")
    #print("hsv area:",hsv(filepath),"mm^2")
    #print("guano area:",area,"mm^2")
'''   
def hsv(filepath):
    image = cv2.imread(filepath)
    #img = cv2.fastNLMeansDenoisingColored(image, None, 3, 3, 7, 21)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv_range = [(0, 55, 55), (15, 255, 255)]
    red = cv2.inRange(hsv_image, hsv_range[0], hsv_range[1])
    red_count = np.count_nonzero(red == 255)
    total_pixels = image.shape[0] * image.shape[1]
    perc_red = red_count / total_pixels
    area = round(71733.51 * perc_red)
    contours,_ = cv2.findContours(red, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            area -= (71733.51*(cv2.contourArea(contour)/total_pixels))
    mask = cv2.bitwise_and(hsv_image, hsv_image, mask=red)
    cv2.imshow("hsv mask",mask)
    cv2.waitKey()
    cv2.destroyAllWindows()
    return area
'''
def bgr(filepath):
    image = cv2.imread(filepath)
    red_range = [(0, 0, 100), (100, 100, 255)]
    red = cv2.inRange(image, red_range[0], red_range[1])
    red_count = np.count_nonzero(red == 255)
    total_pixels = image.shape[0] * image.shape[1]
    perc_red = red_count / total_pixels
    area = round(71733.51 * perc_red)
    #contours, _ = cv2.findContours(red, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    mask = cv2.bitwise_and(image, image, mask=red)
    #cv2.imshow("bgr mask",mask)
    #cv2.imwrite(path, mask)
    #cv2.waitKey()
    #cv2.destroyAllWindows()
    #for contour in contours:
        #if cv2.contourArea(contour) < 700:
            #area -= (71733.51*(cv2.contourArea(contour)/total_pixels))
    return area

if __name__ == "__main__":
    import sys
    main(*sys.argv[1:])
