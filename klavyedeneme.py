from pololu_drv8835_rpi import motors
import math
import keyboard

lx = 0
ly = 0

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
    #raise RuntimeException('bu nasil hayat')
    ly = 0
    try:
        if(keyboard.is_pressed('up')):
            #print("forward")
            ly = -1
        elif(keyboard.is_pressed('down')):
            #print("backward")
            ly = 1
    except:
        print("hata")
    lx = 0
    try:
        if(keyboard.is_pressed('right')):
            #print("right")
            lx = 1
        elif(keyboard.is_pressed('left')):
            #print("left")
            lx = -1
    except:
         print("hata")
    motors.setSpeeds(getValue(lx, ly, True), getValue(lx, ly, False))
