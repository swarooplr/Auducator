import cv2
import numpy as np
import imutils
import json
import model.container as container


class supportingFunctions():

    def __init__(self, context):

        self.context = context
        self.PAGE_HEIGHT = 800
        self.PAGE_WIDTH = 600

        self.COLOUR1L = (29, 86, 60)
        self.COLOUR1H = (64, 255, 255)

        self.COLOUR2L = (0, 100, 100)
        self.COLOUR2H = (179, 255, 255)

        self.TRACKING_RATE = 1

        self.INVERT = 0

        self.CAMERA = 0


        #print(self.context.current_book.book_folder_path)

        #self.values = json.load(open(self.context.current_book.book_folder_path+"/values.json", "r"))
        #self.preferences = json.load(open(self.context.current_book.book_folder_path+"/preferences.json", "r"))

        self.preferences = json.load(open("preferences.json", "r"))
        self.values = json.load(open("values.json", "r"))

        print(self.values,"\n",self.preferences)
        low = self.values["colours"][self.preferences["colour1"]]["low"]
        self.COLOUR1L = (low[0],low[1],low[2])

        high = self.values["colours"][self.preferences["colour1"]]["high"]
        self.COLOUR1H = (high[0],high[1],high[2])

        low = self.values["colours"][self.preferences["colour2"]]["low"]
        self.COLOUR2L = (low[0], low[1], low[2])

        high = self.values["colours"][self.preferences["colour2"]]["high"]
        self.COLOUR2H = (high[0], high[1], high[2])

        print("lol")
        self.PAGE_HEIGHT = int(self.preferences["page_height"])
        self.PAGE_WIDTH = int(self.preferences["page_width"])

        self.TRACKING_RATE = int(self.preferences["tracking_rate"])

        self.INVERT = int(self.preferences["invert"])

        self.CAMERA = int(self.preferences["camera"])
        print("lol")

        print(self.TRACKING_RATE,self.COLOUR1H)


    #greenLower =(29, 86, 60)
    #greenUpper =(64, 255, 255)

    #redLower = (0, 100, 100)
    #redUpper = (179, 255, 255)


    
    def order_points(self,pts): # orders given four points as (tl,tr,br,bl)
    
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
    
        return rect

    def four_point_transform(self,image, rect_pts):   # send image, and corners of rectange in order tl tr br bl   # returns image of rectangle
        rect = rect_pts
        (tl, tr, br, bl) = rect
    
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))
    
    
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))
    
        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype="float32")
    
    
        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
    
        return warped

    def findPage(self,image): #takes image, returns 0 if: page not found , returns page corners if page found
        orig = image.copy()
        cv2.waitKey(self.TRACKING_RATE)
        #image = self.orient_image(image)
        h = 500.0

        ratio = image.shape[0] / h
        image = imutils.resize(image, height=int(h))
    
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        #cv2.imshow('input', gray)
        edged = cv2.Canny(gray, 50, 200)
        #cv2.imshow('canny', edged)
    
        (_, cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]
    
        if (len(cnts) > 0):
            cont = cnts[0]
            if (cv2.contourArea(cont) > (0.2 * image.shape[0] * image.shape[1])):
                peri = cv2.arcLength(cont, True)
                approx = cv2.approxPolyDP(cont, 0.1 * peri, True)
                if len(approx) == 4:
                    screenCnt = approx
                    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)

                    return (True,screenCnt.reshape(4, 2) * ratio,image)
                else:
                    return (False,0,image)
            else:
                return (False,0,image)
        else:
            return (False,0,image)

    def trackColor2(self,frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.COLOUR2L, self.COLOUR2H)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
    
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
    
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    
            if radius > 5:
    
                return center
            else:
                return 0
        else:
            return 0

    def trackColor1(self,frame):
    
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.COLOUR1L, self.COLOUR1H)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
    
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    
        if len(cnts) > 0:
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            if radius > 5:
    
                return center
            else:
                return 0
        else:
            return 0
    
    def getRotatedImage(self,frame, pt):#takes frame and position of red , returns rotated image
        x = pt[1]
        y = pt[0]
        mid_x = int(frame.shape[1] / 2)
        mid_y = int(frame.shape[0] / 2)
        print("red : ", x, y)
        print("mid : ", mid_x, mid_y)
    
        if (x > mid_x and y < mid_y):
            print('1')
            frame = imutils.rotate_bound(frame, 270)
    
        elif (x < mid_x and y > mid_y):
            print('2')
            frame = imutils.rotate_bound(frame, 270)
    
        elif (x > mid_x and y > mid_y):
            print('3')
            frame = imutils.rotate_bound(frame, 180)
    
        else:
            frame = frame
    
        return frame
    
    def imageResize(self,img):
        try:
            h,w,_ = img.shape
            print("size before resize = ",h,"  ",w)
            if(h>w):
                page = cv2.resize(img, (self.PAGE_WIDTH, self.PAGE_HEIGHT), interpolation=cv2.INTER_AREA)
                return page,(self.PAGE_HEIGHT,self.PAGE_WIDTH)
            else:
                page = cv2.resize(img, (self.PAGE_HEIGHT, self.PAGE_WIDTH), interpolation=cv2.INTER_AREA)
                return page, (self.PAGE_WIDTH, self.PAGE_HEIGHT)

        except Exception as e:
            print("Error in image Resize ",type(e).__name__)
    
    def get_working_camera(self):

        if self.CAMERA > 0:
            return self.CAMERA

        for i in range(0,4):
            cap = cv2.VideoCapture(i)
            img = cap.read()
            if img == None:
                continue
            else:
                return i
    
        return None

    def orient_image(self,frame):
        frame = imutils.rotate_bound(frame, self.INVERT)
        return frame

    def get_frame_size(self):
        return self.PAGE_HEIGHT,self.PAGE_WIDTH
