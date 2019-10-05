import serial
import time
import pygame
from desk import *

for i in range(desks_num):
    print "desk", i, ":", desk_x[i], ",", desk_y[i]
display = pygame.display.set_mode( ( 1000, 600 ) )
pygame.display.set_caption("IRA")

try:
    ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout = 1)
except Exception as e:
    try:
        ser = serial.Serial('/dev/ttyUSB1', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout = 1)
    except:
        print("Roboto is not connected !!!")

#########    variebles

done=False
x_robot = 40
y_robot = 30
last_x = x_robot
last_y = y_robot
cmp = 0
c = 0
#########    classes
class distance:
    right = -1
    left = -1
    front = -1
#########    functions
def read_sensors():
    global cmp, last_x, last_y, x_robot, y_robot
    ser.flushInput()
    ser.flushOutput()
    if(ser.read() == 'R'):
        distance.right = (ord(ser.read()) - 48) * 100
        distance.right += (ord(ser.read()) - 48) * 10
        distance.right += (ord(ser.read()) - 48) * 1

    if(ser.read() == 'L'):
        distance.left = (ord(ser.read()) - 48) * 100
        distance.left += (ord(ser.read()) - 48) * 10
        distance.left += (ord(ser.read()) - 48) * 1

    if(ser.read() == 'F'):
        distance.front = (ord(ser.read()) - 48) * 100
        distance.front += (ord(ser.read()) - 48) * 10
        distance.front += (ord(ser.read()) - 48) * 1
    if(ser.read() == 'C'):
        cmp = (ord(ser.read()) - 48) * 100
        cmp += (ord(ser.read()) - 48) * 10
        cmp += (ord(ser.read()) - 48) * 1
    cmp = cmp - c
    if(cmp < -128):
        cmp += 255
    elif(cmp >128):
        cmp -= 255
    cmp *= -4
def draw_lines():
    for i in range(59):
        pygame.draw.line(display,(100,100,255), (10,10 + (i*10)), (790,10 + (i*10)))
    for i in range(79):
        pygame.draw.line(display,(100,100,255), (10+i*10,10), (10+i*10,590))
def draw_wall(x , y):
    pygame.draw.rect(display, (100,100,255), (x*10 , y*10, 10, 10))
def clear_wall(x , y):
    pygame.draw.rect(display, (0,0,0), (x*10 , y*10, 10, 10))
def draw_robot(x,y):
    pygame.draw.rect(display, (0, 0, 0), (last_x*10-10, last_y*10-10, 30, 30))
    pygame.draw.rect(display, (0, 255, 0), (x*10-10, y*10-10, 30, 30))
def draw_desks():
    global cmp, last_x, last_y, x_robot, y_robot
    for i in range(desks_num):
        pygame.draw.rect(display, (255,100,100), (10 + desk_x[i] * 10 , 10 + desk_y[i] * 10, 10, 10))
def set_cmp():
    global cmp, last_x, last_y, x_robot, y_robot, c
    try:
        ser.flushInput()
        ser.flushOutput()
        while(ser.read()!='C'):
            pass
        c = (ord(ser.read()) - 48) * 100
        c += (ord(ser.read()) - 48) * 10
        c += (ord(ser.read()) - 48) * 1
    except:
        pass
def motor(l1,l2,r2,r1, d, next):
    l1 += cmp
    l2 += cmp
    r1 += cmp
    r2 += cmp

    if(l1 > 255): l1 = 255;
    if(l2 > 255): l2 = 255;
    if(r1 > 255): r1 = 255;
    if(r2 > 255): r2 = 255;
    if(l1 < -255): l1 = -255;
    if(l2 < -255): l2 = -255;
    if(r1 < -255): r1 = -255;
    if(r2 < -255): r2 = -255;

    ser.write(b'M')
    ##########      Motor Left 1
    if(l1 >= 0):
        ser.write(b'+')
        b=bytearray()
        b.append((l1/100)%10 + 48)
        b.append((l1/10)%10 + 48)
        b.append((l1/1)%10 + 48)
        ser.write(b)
    else:
        ser.write(b'-')
        b=bytearray()
        b.append((-l1/100)%10 + 48)
        b.append((-l1/10)%10 + 48)
        b.append((-l1/1)%10 + 48)
        ser.write(b)
    ##########      Motor Left 2
    if(l2 >= 0):
        ser.write(b'+')
        b=bytearray()
        b.append((l2/100)%10 + 48)
        b.append((l2/10)%10 + 48)
        b.append((l2/1)%10 + 48)
        ser.write(b)
    else:
        ser.write(b'-')
        b=bytearray()
        b.append((-l2/100)%10 + 48)
        b.append((-l2/10)%10 + 48)
        b.append((-l2/1)%10 + 48)
        ser.write(b)
    ##########      Motor Right 2
    if(r2 >= 0):
        ser.write(b'+')
        b=bytearray()
        b.append((r2/100)%10 + 48)
        b.append((r2/10)%10 + 48)
        b.append((r2/1)%10 + 48)
        ser.write(b)
    else:
        ser.write(b'-')
        b=bytearray()
        b.append((-r2/100)%10 + 48)
        b.append((-r2/10)%10 + 48)
        b.append((-r2/1)%10 + 48)
        ser.write(b)
    ##########      Motor Right 1
    if(r1 >= 0):
        ser.write(b'+')
        b=bytearray()
        b.append((r1/100)%10 + 48)
        b.append((r1/10)%10 + 48)
        b.append((r1/1)%10 + 48)
        ser.write(b)
    else:
        ser.write(b'-')
        b=bytearray()
        b.append((-r1/100)%10 + 48)
        b.append((-r1/10)%10 + 48)
        b.append((-r1/1)%10 + 48)
        ser.write(b)
    d = (d*1000)//527
    b=bytearray()
    b.append((d/100)%10 + 48)
    b.append((d/10)%10 + 48)
    b.append((d/1)%10 + 48)
    ser.write(b)
    b=bytearray()
    b.append(next)
    ser.write(b)
    cnt = 0
    while ser.read() != 'A':
        cnt += 1
        if cnt > 100:
            break

set_cmp()
while not done:
    try:
        read_sensors()
        for i in range(distance.right//10 - 1):
            clear_wall(x_robot + i , y_robot)
        for i in range(distance.left//10 - 1):
            clear_wall(x_robot - i , y_robot)
        for i in range(distance.front//10 - 1):
            clear_wall(x_robot , y_robot - i)
        draw_wall(x_robot + distance.right//10, y_robot)
        draw_wall(x_robot - distance.left//10, y_robot)
        draw_wall(x_robot, y_robot - distance.front//10)
    except:
        try:
            ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout = 1)
        except:
            pass
    draw_lines()
    draw_desks()
    draw_robot(x_robot, y_robot)

    # print distance.left, distance.front, distance.right, cmp
    last_x = x_robot
    last_y = y_robot
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                motor(200,200,-200,-200,10,'S')
                y_robot -= 1
            if event.key == pygame.K_DOWN:
                motor(-200,-200,200,200,10,'S')
                y_robot += 1
            if event.key == pygame.K_LEFT:
                motor(-200,200,200,-200,10,'S')
                x_robot -= 1
            if event.key == pygame.K_RIGHT:
                motor(200,-200,-200,200,10,'S')
                x_robot += 1
            if event.key == pygame.K_s:
                set_cmp()
