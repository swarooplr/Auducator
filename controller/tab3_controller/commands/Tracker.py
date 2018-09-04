import  cv2
import numpy as np
import imutils
import controller.supportingFunctions as supporting_functions


cordinates=(0,0)

global SF


def track(orientationCorrection,context): #true to correct false to avoid orientaion correction

    SF = supporting_functions.supportingFunctions(context)
    camera_id = SF.get_working_camera()
    if not camera_id == None:
        cap = cv2.VideoCapture(camera_id)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)

    else:
        pass  # through error here

    pageFound = False
    points = 0

    while True:

        ret, image = cap.read()
        image = SF.orient_image(image)
        key = cv2.waitKey(1) & 0xFF
        condition, pageCorners, pageBordered = SF.findPage(image)
        if( not pageFound):
            if (not condition):
                cv2.putText(pageBordered, "Unable to find page: press e to exit", (15, 15), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 1)
                cv2.imshow("camera", pageBordered)

            else:
                points = SF.order_points(pageCorners)
                pageFound = True

        else:

            pageCrop = SF.four_point_transform(image, points)
            pageCrop,_ = SF.imageResize(pageCrop)
            #if(not orientationCorrection == 0):
            #    pageCrop = imutils.rotate_bound(pageCrop, orientationCorrection)
            pageCropDisplay = pageCrop.copy()

            marker = SF.trackColor1(pageCrop)
            if marker == 0:
                cv2.putText(pageCropDisplay, "Unable to find marker: E to exit", (15, 15), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 1)
                cv2.imshow("camera", pageCropDisplay)

            else:
                cv2.putText(pageCropDisplay, "Tracking: E to exit : R to reset page", (15, 15), cv2.FONT_HERSHEY_SIMPLEX,
                            0.5, (255, 255, 255), 1)
                cv2.circle(pageCropDisplay, marker, 5, (0, 0, 255), -1)
                cv2.imshow("camera", pageCropDisplay)

                global cordinates
                cordinates = marker
                #print(marker)
                #print(marker)

        if key == ord("e"):
            cv2.destroyAllWindows()
            cordinates = (-1000,-1000)
            return


        if key == ord("r"):
            pageFound = False



