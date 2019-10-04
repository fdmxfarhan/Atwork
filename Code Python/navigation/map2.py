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
    print("Roboto is not connected !!!")

#########    variebles

done=False
x_robot = 400
y_robot = 300
last_x = x_robot
last_y = y_robot


#########    functions

def read_distance():
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
def draw_lines():
    for i in range(59):
        pygame.draw.line(display,(100,100,255), (10,10 + (i*10)), (790,10 + (i*10)))
    for i in range(79):
        pygame.draw.line(display,(100,100,255), (10+i*10,10), (10+i*10,590))
def draw_wall(x , y):
    pygame.draw.rect(display, (100,100,255), (x , y, 10, 10))
def draw_robot(x,y):
    pygame.draw.rect(display, (255, 255, 255), (last_x-10, last_y-10, 30, 30))
    pygame.draw.rect(display, (0, 255, 0), (x-10, y-10, 30, 30))
def draw_desks():
    for i in range(desks_num):
        pygame.draw.rect(display, (255,100,100), (10 + desk_x[i] * 10 , 10 + desk_y[i] * 10, 10, 10))

while not done:
    try:
        read_distance()
    except:
        pass
    draw_lines()
    draw_desks()
    draw_robot(x_robot, y_robot)


    last_x = x_robot
    last_y = y_robot
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
