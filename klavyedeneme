import pygame
from pololu_drv8835_rpi import motors
import math
import sys
import picamera
import termios
import tty
pygame.init()


##camera = picamera.PiCamera()
lx = 0
ly = 0
i = 0

##camera.resolution = (1920, 1080)

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
    ch = ""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    if(ch == "w"):
        lx = -1
        ly = -1
    elif(ch == "s"):
        lx = 1
        ly = 1
    elif(ch == "a"):
        lx = 1
        ly = -1 
    elif(ch == "d"):
        lx = -1
        ly = 1
    else:
        lx = 0
        ly = 0
      
    motors.setSpeeds(getValue(lx, ly, True), getValue(lx, ly, False))
