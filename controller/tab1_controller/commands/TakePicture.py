import controller.tab1_controller.commands as commands
import controller.tab1_controller.commands as commands
import cv2
import numpy as np
from PyQt5.QtWidgets import QMessageBox
import imutils
from PyQt5.QtGui import QIcon, QPixmap
import cv2

class TakePictureCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None, dialog = None):
        self.context = context
        self.gui = gui
        self.dialog = dialog

    def execute(self):
        print(self)
        try:
            #print(self.context.current_book.book_folder_path)
            img = self.pageSelector()
            img, dimen = self.context.SF.imageResize(img)
            cv2.imwrite("selectedImage.png", img)
            print('image saved')
            self.dialog.Page_view.setPixmap(QPixmap("selectedImage.png"))
        except Exception as e:
            print("couldnt get page ",type(e).__doc__)

    def unexcute(self):
        print(self)



    def pageSelector(self):
        pageDetected = False
        marker = 0

        camera_id = self.context.SF.get_working_camera()
        print("working camera = " , camera_id)
        if not camera_id == None:
            cap = cv2.VideoCapture(camera_id)

            h, w = self.context.SF.get_frame_size()
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)

        else:
            QMessageBox.about(self.gui, "Error", "No camera detected")
            print("camera error")

        while True:
            key = cv2.waitKey(1) & 0xFF

            ret, image = cap.read()
            image = self.context.SF.orient_image(image)
            orig = image.copy()
            final = orig


            condition, pageCorners, pageBordered = self.context.SF.findPage(image)

            if (not condition):

                cv2.putText(pageBordered, "Page not detected -  press E to complete", (15, 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                final = pageBordered

            else:

                cv2.putText(pageBordered, "Press Q if page is selected properly - press E to complete", (15, 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                final = pageBordered

                if (pageDetected):
                    points = self.context.SF.order_points(pageCorners)
                    pageCrop = self.context.SF.four_point_transform(image, points)
                    pageCrop, _ = self.context.SF.imageResize(pageCrop)
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
                    img, _ = self.context.SF.imageResize(pageCrop)
                else:
                    img, _ = self.context.SF.imageResize(orig)

                return img

            ''' Future work 
                       if key == ord("o"):
                           cv2.destroyAllWindows()
                           img,_ = self.context.SF.imageResize(pageCropOrig)
                           return img
            
            '''

                    


