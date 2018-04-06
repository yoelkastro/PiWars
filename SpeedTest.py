from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from pololu_drv8835_rpi import motors
import pygame
import sys

camera = PiCamera()

pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()

##
camera.resolution = (640, 480)
camera.framerate = 100
rawCapture = PiRGBArray(camera, size=(640, 480))
motors.setSpeeds(0, 0)
time.sleep(0.1)
rainbow_lower = [[4,31,120],[31,76,4],[76,31,4]]
#[30,104,104],[31,76,4],[76,31,4]
rainbow_upper = [[70,90,210],[90,210,70],[190,90,70]]
#[50,240,241],[90,210,70],[190,90,70]]

while True:
        for e in pygame.event.get():
                if(e.type == pygame.JOYBUTTONDOWN):
                        if(e.button == 12):
                                sys.exit()
                        elif(e.button == 14):
                                color = 0
                                for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    
                                        image = frame.array

                                        blur = cv2.blur(image, (3,3))

                                        
                                        lower = np.array(rainbow_lower[color],dtype="uint8")
                                        upper = np.array(rainbow_upper[color], dtype="uint8")
        
                                        thresh = cv2.inRange(blur, lower, upper)
        
                                        image, contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                                        max_area = 0
                                        best_cnt = 1
                                        for cnt in contours:
                                                area = cv2.contourArea(cnt)
                                                if area > max_area:
                                                       max_area = area
                                                       best_cnt = cnt

                                        M = cv2.moments(best_cnt)
                                        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
                                        rawCapture.truncate(0)

                                        if(cx < 380 and cx > 260):
                                            print('yes')
                                            motors.setSpeeds(400, 420)
                                            time.sleep(0.5)
                                            motors.setSpeeds(-420, -400)
                                            time.sleep(0.5)
                                            motors.setSpeeds(0, 0)
                                            color = color + 1
                                            if(color == 4):
                                                    break
                                                
                                        else:
                                            motors.motor1.setSpeed(175)
                                            motors.motor2.setSpeed(-175)
                                        for e in pygame.event.get():
                                                if(e.type == pygame.JOYBUTTONDOWN):
                                                        if(e.button == 12):
                                                                sys.exit()
        

