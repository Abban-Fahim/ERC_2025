import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread("./balls/1.png");
cv2.namedWindow("circles")
cv2.createTrackbar("param1", "circles", 50, 100, nothing)
cv2.createTrackbar("param2", "circles", 50, 100, nothing)
cv2.createTrackbar("minDist", "circles", 50, 600, nothing)
cv2.createTrackbar("dp", "circles", 1, 5, nothing)

cv2.namedWindow("edges")
cv2.createTrackbar("t1", "edges", 1, 500, nothing)
cv2.createTrackbar("t2", "edges", 1, 500, nothing)


while True:
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurImg = cv2.GaussianBlur(grayImg, (7, 7), 5)

    t1 = cv2.getTrackbarPos("t1", "edges")
    t2 = cv2.getTrackbarPos("t2", "edges")
    edges = cv2.Canny(blurImg, t1, t2)

    param1 = cv2.getTrackbarPos("param1", "circles")
    param2 = cv2.getTrackbarPos("param2", "circles")
    minDist = cv2.getTrackbarPos("minDist", "circles")
    dp = cv2.getTrackbarPos("dp", "circles")
    print(param1, param2, minDist)
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=dp, minDist=minDist, param1=param1, param2=param2)
    
    vizImg = img.copy()
    if circles is not None:
        for c in circles[0, :]:
            # print(c)
            vizImg = cv2.circle(vizImg, (int(c[0]), int(c[1])), int(c[2]), (0,0,255), 3)
    cv2.imshow("meow", img)
    cv2.imshow("edges", edges)
    cv2.imshow("vizImg", vizImg)

    code = cv2.waitKey(1) & 0xFF
    if code == 27:
        break;

cv2.destroyAllWindows()