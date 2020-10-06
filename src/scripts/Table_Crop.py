import cv2
import numpy as np
import PyQt5
cropping = False

x_start, y_start, x_end, y_end = 0, 0, 0, 0

image = cv2.imread('Citibank.png')
#image = cv2.imread('Morgan Stanley.png')
#image = cv2.imread('UBS Global.png')


oriImage = image.copy()

def mouse_crop(event, x, y, flags, param):
    # grab references to the global variables
    global x_start, y_start, \
        x_end, y_end, cropping

    # if the left mouse button was DOWN, start RECORDING
    # (x, y) coordinates and indicate that cropping is being
    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True

    # Mouse is Moving
    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y

    # if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates
        x_end, y_end = x, y
        cropping = False  # cropping is finished

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2:  # when two points were found
            roi = oriImage[refPoint[0][1]:refPoint[1][1], refPoint[0][0]:refPoint[1][0]]
            im = cv2.resize(roi, (1440, 800))
            cv2.imshow("Cropped", im)
            #cv2.imwrite('Citibank_Crop1.png', im)
            #im2 = cv2.resize(roi, (,))
            cv2.imwrite('Citibank_Crop.png', roi)
            #cv2.imwrite('Morgan Stanley_Crop.png', roi)
            #cv2.imwrite('Morgan Stanley_Crop.png', roi)

#cv2.namedWindow("image")
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setMouseCallback("image", mouse_crop)

def table_crop():
    while True:

        i = image.copy()

        if not cropping:
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            cv2.imshow("image", image)

        elif cropping:
            cv2.rectangle(i, (x_start, y_start), (x_end, y_end), (255, 0, 0), 2)
            cv2.namedWindow('image', cv2.WINDOW_NORMAL)
            cv2.imshow("image", i)

        cv2.waitKey(1)


# close all open windows
#cv2.destroyAllWindows()