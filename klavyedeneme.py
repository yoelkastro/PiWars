from pololu_drv8835_rpi import motors
import math
import sys
import keyboard

lx = 0
ly = 0
i = 0


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

    ly = 0
    if(keyboard.is_pressed('w')):
        print("forward")
        ly = -1
    elif(keyboard.is_pressed('s')):
        print("backward")
        ly = 1

    lx = 0
    if(keyboard.is_pressed('a')):
        print("right")
        lx = -1
    elif(keyboard.is_pressed('d')):
        print("left")
        lx = 1
     
    motors.setSpeeds(getValue(lx, ly, True), getValue(lx, ly, False))
