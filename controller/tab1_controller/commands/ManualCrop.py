import controller.tab1_controller.commands as commands
import cv2
import numpy as np
import cv2
from PyQt5.QtGui import QIcon, QPixmap

class ManualCropCommand(commands.BaseCommand):

    def __init__(self,context=None, gui=None,dialog = None):
        self.context = context
        self.gui = gui
        self.dialog = dialog

    def execute(self):
        print(self)
        try:
            img = self.MC("selectedImage.png")
            cv2.imwrite("selectedImage.png", img)
            print('image saved')
            self.dialog.Page_view.setPixmap(QPixmap("selectedImage.png"))
        except:
            print("crop failed")

    def unexcute(self):
        print(self)


    def MC(self,path):

        refPt = []
        #corners = ((0, 0))
        #cropping = False

        def click_saver(event, x, y, flags, param):
            global reft
            if event == cv2.EVENT_LBUTTONUP:
                pt = list()
                pt.append(x)
                pt.append(y)
                refPt.append(pt)
                cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
                cv2.imshow("image", image)

        def ManualCropper(path):
            global image
            image = cv2.imread(path)
            clone = image.copy()
            cv2.putText(image, "Click on the four Corners of the page, R to reset ", (15, 15), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 1)
            cv2.namedWindow("image")
            cv2.setMouseCallback("image", click_saver)

            while True:
                cv2.imshow("image", image)
                key = cv2.waitKey(1) & 0xFF

                if key == ord("r"):
                    refPt.clear()
                    image = clone.copy()
                    cv2.putText(image, "Click on the four Corners of the page, R to reset ", (15, 15),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

                if key == ord("c"):
                    cv2.destroyWindow("image")
                    break

                if (len(refPt) == 4):
                    cv2.destroyWindow("image")
                    break

            # cv2.waitKey(0)
            # cv2.destroyAllWindows()

            # print(refPt)
            arr = np.array(refPt, dtype="float32")
            points = self.context.SF.order_points(arr)

            pageCrop = self.context.SF.four_point_transform(clone, points)

            return pageCrop

        img = ManualCropper(path)
        return img