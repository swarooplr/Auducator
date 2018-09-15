import cv2
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import imutils
from PyQt5.QtGui import QIcon, QPixmap
import cv2


class VisionModules():

    def __init__(self,SF):
        self.SF = SF

    def pageSelector(self):
        pageDetected = False
        marker = 0

        camera_id = self.SF.get_working_camera()
        print("working camera = ", camera_id)
        if not camera_id == None:
            cap = cv2.VideoCapture(camera_id)

            h, w = self.SF.get_frame_size()
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)

        else:
            return None


        while True:
            key = cv2.waitKey(1) & 0xFF

            ret, image = cap.read()
            image = self.SF.orient_image(image)
            orig = image.copy()
            final = orig

            condition, pageCorners, pageBordered = self.SF.findPage(image)

            if (not condition):

                cv2.putText(pageBordered, "Page not detected -  press E to complete", (15, 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                final = pageBordered

            else:

                cv2.putText(pageBordered, "Press Q if page is selected properly - press E to complete", (15, 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                final = pageBordered

                if (pageDetected):
                    points = self.SF.order_points(pageCorners)
                    pageCrop = self.SF.four_point_transform(image, points)
                    pageCrop, _ = self.SF.imageResize(pageCrop)
                    final = pageCrop

                    '''This part is for future implementation
                    marker = self.context.SF.trackColor2(pageCrop)
                    if marker == 0:
                        cv2.putText(pageCrop, "Orientation correction failed, press E to complete", (15, 15),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                    else:
                        pageCrop = self.context.SF.getRotatedImage(pageCrop, marker)

                        cv2.putText(pageCrop, "Press O if orientations is correct - press E to complete", (15, 15),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                        cv2.imshow("Page", pageCrop)
                        pageCropOrig = pageCrop
                    '''

            cv2.imshow("Take Picture", final)

            if key == ord("q"):
                pageDetected = True

            if key == ord("e"):
                cv2.destroyAllWindows()
                if pageDetected:
                    img, _ = self.SF.imageResize(pageCrop)
                else:
                    img, _ = self.SF.imageResize(orig)


                return img


            ''' Future work 
                       if key == ord("o"):
                           cv2.destroyAllWindows()
                           img,_ = self.context.SF.imageResize(pageCropOrig)
                           return img

            '''

    def trackMarker(self):

        camera_id = self.SF.get_working_camera()
        if not camera_id == None:
            cap = cv2.VideoCapture(camera_id)
            h, w = self.SF.get_frame_size()
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)

        else:
            return None


        while True:

            ret, image = cap.read()
            image = self.SF.orient_image(image)
            final = image
            key = cv2.waitKey(1) & 0xFF

            marker = self.SF.trackColor1(image)
            if marker == 0:
                cv2.putText(image, "Unable to find marker: E to exit", (15, 15), cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (255, 255, 255), 1)

            else:
                cv2.putText(image, "Tracking: E to exit : R to reset page", (15, 15),
                                cv2.FONT_HERSHEY_SIMPLEX,
                                0.5, (255, 255, 255), 1)
                cv2.circle(image, marker, 5, (0, 0, 255), -1)
            cv2.imshow("Tracking", image)

            if key == ord("e"):
                cv2.destroyAllWindows()
                return image

