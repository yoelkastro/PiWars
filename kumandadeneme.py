import pygame
from pololu_drv8835_rpi import motors
import math
import sys
import picamera
pygame.init()
pygame.joystick.init()

j = pygame.joystick.Joystick(0)
j.init()
camera = picamera.PiCamera()
lx = 0
ly = 0
i = 0

camera.resolution = (1920, 1080)

def getValue(x, y, t):
    if(t):
        if(math.copysign(1, x) != math.copysign(1, y)):
            return (int)((-y + x) * 240)
        else:
            return (int)((-y + x) * 480)
    else:
        if(math.copysign(1, x) == math.copysign(1, y)):
            return (int)((-y - x) * 240)
        else:
            return (int)((-y - x) * 480)

while True:
    record = False
    for e in pygame.event.get():
        if(e.type == pygame.JOYAXISMOTION):
            if(e.axis == 0):
                lx = e.value
            elif(e.axis == 1):
                ly = e.value
        if(e.type == pygame.JOYBUTTONDOWN):
            if(e.button == 14):
                string = 'fizliresim'
                string += str(i)
                string += '.jpg'
                camera.capture(string)
                i = i + 1
            elif(e.button == 12):
                string = 'video.h264'
                if record:
                    camera.stop_recording()
                    record = False
                else:
                    camera.start_recording(string)
                    record = True
            else:
                sys.exit()
        
    motors.setSpeeds(getValue(lx, ly, True), getValue(lx, ly, False))
