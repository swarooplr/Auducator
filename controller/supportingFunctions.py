import cv2
import numpy as np
import imutils

greenLower =(29, 86, 60)
greenUpper =(64, 255, 255)

redLower = (0, 100, 100)
redUpper = (179, 255, 255)


def order_points(pts): # orders given four points as (tl,tr,br,bl)

    rect = np.zeros((4, 2), dtype="float32")
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect




def four_point_transform(image, rect_pts):   # send image, and corners of rectange in order tl tr br bl   # returns image of rectangle
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


def findPage(image): #takes image, returns 0 if: page not found , returns page corners if page found
    orig = image.copy()
    ratio = image.shape[0] / 500.0
    image = imutils.resize(image, height=500)

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
                #warped = four_point_transform(orig,order_points(screenCnt.reshape(4, 2) * ratio))
                #cv2.imshow("Image - page", orig)
                #cv2.imshow("page - warped", warped)
                #return (False, 0, 0)
                return (True,screenCnt.reshape(4, 2) * ratio,image)
            else:
                return (False,0,image)
        else:
            return (False,0,image)
    else:
        return (False,0,image)



def trackColor2(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, redLower, redUpper)
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


def trackColor1(frame):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, greenLower, greenUpper)
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

def getRotatedImage(frame, pt):#takes frame and position of red , returns rotated image
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

def imageResize(img):
    h,w,_ = img.shape
    if(h>w):
        page = cv2.resize(img, (600, 800), interpolation=cv2.INTER_AREA)
        return page,(800,600)
    else:
        page = cv2.resize(img, (800, 600), interpolation=cv2.INTER_AREA)
        return page, (600, 800)

def get_working_camera():

    for i in range(0,4):
        cap = cv2.VideoCapture(i)
        img = cap.read()
        if img == None:
            continue
        else:
            return 2

    return None