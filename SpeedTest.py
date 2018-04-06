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
isMove = 1

while True:
        for e in pygame.event.get():
                if(e.type == pygame.JOYBUTTONDOWN):
                        if(e.button == 12):
                                sys.exit()
                        elif(e.button == 14):
                                for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
                          
                                        image = frame.array

                                        blur = cv2.blur(image, (3,3))

                                        
                                        lower = np.array([0, 0, 0], dtype="uint8")
                                        upper = np.array([20, 20, 20], dtype="uint8") #white
        
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

                                        motors.setSpeeds(
                                               ((1.125 * cx + 120) * fabs(floor(cx / 320) - 1)) + (480 * fabs(floor(cx / 320))) * isMove, #left
                                               ((- 1.125 * cx + 840) * fabs(floor(cx / 320))) + (480 * fabs(floor(cx / 320) - 1)) * isMove #right
                                        )
                                        for e in pygame.event.get():
                                                if(e.type == pygame.JOYBUTTONDOWN):
                                                        if(e.button == 12):
                                                                isMove = 0
                                                        elif(e.button = 14):
                                                                isMove = 1
        

