import cv2
import numpy as np

image = cv2.imread('IMG-20260831-WA0029.jpg')

# convert the imagr to grayscale
gray_image = cv2.cvtcolor(image , cv2.COLOR_BGR2GRAY)

def load_image(image_path):
    image = cv2.imread(image_path)

    if image is none:
        raise Filenotfounderror(f"could not load image: {image_path}"
        )
    return image



def create_traversable_mask(image):

    # convert BGR -> HSV
    hsv = cv2.cvtcolor(image, cv2.COLOR_BGR2HSV )

    # green colour range
    lower_green = np.array([40,40,40])
    upper_green = np.array([70,255,255])

    mask = cv2.inrange(hsv, lower_green, upper_green)

    return mask






def create_obstacle_mask(image):

    hsv = cv2.cvtcolor(image, cv2.COLOR_BGR2HSV)

    #  black pixels 
    lower_black = np.array([0,0,0])
    upper_black = np.array([180,225,30])

    mask = cv2.inrange(hsv, lower_black, upper_black)


    return mask



def  find_start(image):

    hsv = cv2.cvtcolor(image, cv2.COLOR_BGR2HSV)

    lower_orange = np.array([10,100,20])

    mask = cv2.inrange(hsv, lower_orange, upper_orange )

    countours, _ = cv2.findcontours(mask, cv2.RETER_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if not countours:
        return None

    contour = max(contour, key=cv2.contourArea)

    M = cv2.moments(contour)

    if M["m00"] == 0:

        return (x , y)


def finf_destination(image):



    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV): 



    lower_purple = np.array([130, 50, 50])
    upper_purple = np.array([160, 255, 255])

    mask = cv2.inrange(
        hsv,
        lower_purple,
        upper_purple
    )

    contours, _ = cv2.findContours(
        mask,
        cv2.RETER_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    if not contours:
        return None

    contour = max(contours, key=cv2.contourArea)

    M = cv2.moments(contour)

    if M["m00"] == 0:
        return None

    x = int(M["m10"] / M["m00"])
    y = int(M["m01"] / M["m00"])

    return (x,y)





def save_mask(mask, output_path):

    cv2.imwrite(
        output_path,
        mask
        )
    




