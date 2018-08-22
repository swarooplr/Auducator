import controller.tab1_controller.commands as commands
import cv2
import numpy as np
import imutils
import controller.supportingFunctions as Sp
from PyQt5.QtGui import QIcon, QPixmap
import cv2

class TakePictureCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None):
        self.context = context
        self.gui = gui

    def execute(self):
        print(self)
        try:
            #print(self.context.current_book.book_folder_path)
            self.SF = Sp.supportingFunctions(self.context)
            img = self.pageSelector()
            cv2.imwrite("selectedImage.png", img)
            print('image saved')
            self.gui.tab1_page_view.setPixmap(QPixmap("selectedImage.png"))
        except Exception as e:
            print("couldnt get page ",type(e).__name__)

    def unexcute(self):
        print(self)



    def pageSelector(self):
        pageDetected = False
        marker = 0

        camera_id = self.SF.get_working_camera()
        print("working camera = " , camera_id)
        if not camera_id == None:
            cap = cv2.VideoCapture(camera_id)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)


        else:
            print("camera error") #through exception


        while True:


            ret, image = cap.read()
            orig = image.copy()

            key = cv2.waitKey(1) & 0xFF

            condition, pageCorners, pageBordered = self.SF.findPage(image)

            if (not condition):

                cv2.putText(pageBordered, "Page not detected -  press E to complete", (15, 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.imshow("camera", pageBordered)


            else:

                cv2.putText(pageBordered, "Press Q if page is selected properly - press E to complete", (15, 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                cv2.imshow("camera", pageBordered)

                if (pageDetected):
                    points = self.SF.order_points(pageCorners)

                    pageCrop = self.SF.four_point_transform(image, points)
                    pageCropOrig = pageCrop.copy()
                    pageCrop, _ = self.SF.imageResize(pageCrop)
                    marker = self.SF.trackColor2(pageCrop)

                    if marker == 0:

                        cv2.putText(pageCrop, "Orientation correction failed, press E to complete", (15, 15),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                        pageCrop = imutils.rotate_bound(pageCrop, 180)  ###remove this shit
                        cv2.imshow("Page", pageCrop)  ###remove this shit
                        cv2.imwrite("page101.jpg", pageCrop)  ###remove this shit
                    else:
                        pageCrop = self.SF.getRotatedImage(pageCrop, marker)

                        cv2.putText(pageCrop, "Press O if orientations is correct - press E to complete", (15, 15),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                        cv2.imshow("Page", pageCrop)
                        pageCropOrig = pageCrop

            if key == ord("q"):
                pageDetected = True

            if key == ord("o"):
                cv2.destroyAllWindows()
                return pageCropOrig

            if key == ord("e"):
                cv2.destroyAllWindows()
                if pageDetected:
                    return pageCropOrig
                else:
                    return orig
                    


