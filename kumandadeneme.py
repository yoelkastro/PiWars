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

GPIO.setup(18, GPIO.OUT)
golfServo = GPIO.PWM(18, 180)
golfServo.start(5)
golfAngle = 0

camera.resolution = (1920, 1080)

def shoot():

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
    buttons = []
    for e in pygame.event.get():
        if(e.type == pygame.JOYAXISMOTION):
            if(e.axis == 0):
                lx = e.value
            elif(e.axis == 1):
                ly = e.value
        if(e.type == pygame.JOYBUTTONDOWN):
            
            buttons.append(e.button)
            
            #else:
                #sys.exit()
        
    motors.setSpeeds(getValue(lx, ly, True), getValue(lx, ly, False))
    
    if 14 in buttons:
        shoot()
    if R2 in buttons:
        if golfAngle > 0:
            golfAngle -= 10
            golfServo.ChangeDutyCycle(golfAngle)
    if L2 in buttons:
        if golfAngle < 180:
            golfAngle += 10
            golfServo.ChangeDutyCycle(golfAngle)
