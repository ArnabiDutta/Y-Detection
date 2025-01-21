import cv2 as cv
# import mediapipe as mp
# import time
import numpy as np
# import math



Y=cv.imread("E:\\Kardarshev Scale\\Resources\\hee side.jpeg")
# Yresize=cv.resize(Y,(400,600))
Y_bw=cv.cvtColor(Y,cv.COLOR_BGR2GRAY)
Y_canny=cv.Canny(Y_bw,150,200)
Y_contours,hierarchy=cv.findContours(Y_canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
# print(Y_contours)
for Y_contour in Y_contours:
        cv.drawContours(Y,[Y_contour],-1,(0,255,0),2)


cap=cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success,img=cap.read()
    img_bw=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    blur = cv.bilateralFilter(img_bw,9,75,75)

    img_canny=cv.Canny(blur,300,350)
    kernel = np.ones((5,5),np.uint8)
    dillated = cv.dilate(img_canny, kernel)

    contours, hierarchy=cv.findContours(dillated,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    # n=0
    for contour in contours:
        # n+=1
        area=cv.contourArea(contour)
        # cv.drawContours(img,[contour],-1,(0,255,0),2)
        # if Y_contours:
        a=cv.matchShapes(Y_contours[0],contour,1,0.0)
        # for c in contours[0]:
        if a<0.4 and area>500:
            # print(a)
            cv.drawContours(img,[contour],-1,(0,255,0),2)

            cv.circle(img,(60,55),3,(0,128,0),-1)
        
            
            epsilon=0.02*cv.arcLength(contour,True)
            approx=cv.approxPolyDP(contour,epsilon,True)
            # x1=approx.ravel()[6]     
            # y1=approx.ravel()[7]
            # x2=approx.ravel()[4]     
            # y2=approx.ravel()[5]  
           

            # px=(x1+x2)//2
            # py=(y1+y2)//2
            # [vx,vy,x,y] = cv.fitLine(contour, cv.DIST_L2,0,0.01,0.01)
            # rows,cols = img.shape[:2]
            # lefty = int((-x*vy/vx) + y)
            # righty = int(((cols-x)*vy/vx)+y)
            # cv.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

            M=cv.moments(approx)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv.circle(img, (cx, cy), 5, (0, 0, 0), -1)

            rect=cv.minAreaRect(contour)
            box = cv.boxPoints(rect)
            box = np.int0(box)
            # print(box)
            cv.drawContours(img,[box],0,(0,0,255),2)

        

            # cv.circle(img,(boxcx,boxcy),3,(0,0,0),3)

            Angle=int(rect[2])
            # print(rect)
            if rect[1][1]>rect[1][0]:
                Angle=90+Angle
            if Angle < 0:  # convert negative angles to positive
                Angle += 360
                cv.putText(img,str(Angle),(cx,cy+70),cv.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)
            if Angle < 0:  # convert negative angles to positive
                Angle += 360
                cv.putText(img,str(Angle),(cx,cy+70),cv.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)
            Angle = (Angle + 360) % 360


            # else:  
            #     cv.putText(img,f'Angle={str(int(rect[2])+90)}',(cx,cy+70),cv.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)
                
            # height>width -90
           

            # cv.circle(img,(cx,cy),3,(100,100,100),3)
            # cv.circle(img,(x1,y1),3,(0,100,100),3)
            # cv.circle(img,(x2,y2),3,(0,100,100),3)
            # cv.circle(img,(px,py),3,(0,100,100),3)
            # cv.line(img,(cx,cy),(px,py),(255,255,255),2)

            

            # angle=str(int(np.degrees(np.arctan((py-cy)/(px-cx))))-90)   
            # cv.putText(img,f'Angle={angle}',(px,py+70),cv.FONT_HERSHEY_PLAIN,1.5,(0,0,0),2) 

        else:
            cv.circle(img,(60,55),3,(1000,0,0),-1)



    cv.imshow("W",img)
    # cv.imshow("hhh",img_canny)
    cv.imshow("p",Y)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break