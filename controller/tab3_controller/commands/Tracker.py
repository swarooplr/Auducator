import  cv2
import numpy as np
import imutils
import controller.supportingFunctions as supporting_functions
from PyQt5.QtWidgets import QMessageBox


cordinates=(0,0)

global SF


def track(context,gui):

    SF = supporting_functions.supportingFunctions(context)
    camera_id = SF.get_working_camera()
    if not camera_id == None:
        cap = cv2.VideoCapture(camera_id)
        h,w = SF.get_frame_size()
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)

    else:
        QMessageBox.about(gui, "Error", "No camera detected, \nPlease try changing the camera port in settings ")
        print("camera error")

    pageFound = False
    points = 0

    while True:

        #this is condition is checked ,so that even on click of stop button the cv2 window is destroyed.
        if cordinates == (-1000,-1000):
            cv2.destroyAllWindows()
            return

        ret, image = cap.read()
        image = SF.orient_image(image)
        final = image
        key = cv2.waitKey(1) & 0xFF
        condition, pageCorners, pageBordered = SF.findPage(image)
        if(not pageFound):
            if (not condition):
                cv2.putText(pageBordered, "Unable to find page: press SPACE BAR to exit", (15, 15), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 1)
                final =  pageBordered

            else:
                points = SF.order_points(pageCorners)
                pageFound = True
                continue

        else:
            #points = SF.order_points(pageCorners)
            pageCrop = SF.four_point_transform(image, points)
            pageCrop,_ = SF.imageResize(pageCrop)

            pageCropDisplay = pageCrop.copy()

            marker = SF.trackColor1(pageCrop)
            if marker == (-1,-1):
                cv2.putText(pageCropDisplay, "Unable to find marker: SPACE BAR to exit", (15, 15), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 1)

            else:
                cv2.putText(pageCropDisplay, "Tracking: SPACE BAR to exit : R to reset page", (15, 15), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 1)
                cv2.circle(pageCropDisplay, marker, 5, (0, 0, 255), -1)

            final = pageCropDisplay

            global cordinates
            cordinates = marker
                #print(marker)
                #print(marker)

        cv2.imshow("Tracking", final)

        if key == ord(" "):
            cv2.destroyAllWindows()
            cordinates = (-1000,-1000)
            return


        if key == ord("r"):
            pageFound = False







