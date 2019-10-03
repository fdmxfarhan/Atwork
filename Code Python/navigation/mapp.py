import serial
import time
import pygame

display = pygame.display.set_mode((800,600))
pygame.display.set_caption('IRA')
map = pygame.image.load('new_map.jpg')
display.blit(map, (0,0))

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout = 1)
#########################################################################################
x_robot = 400
y_robot = 300
direction = 's'
done = False

#########################################################################################
class distance:
    right = -1
    left = -1
    front = -1

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
    # distance.left *= 2
    # distance.right *= 2
    # distance.front *= 2

def move(dir):
    if(dir == 1): ser.write(b'M+000+000-255-255')
    elif(dir == 2): ser.write(b'M+100+100-255-255')
    elif(dir == 3): ser.write(b'M+150+150-255-255')
    elif(dir == 4): ser.write(b'M+255+255-255-255') #forward
    elif(dir == 5): ser.write(b'M+255+255-150-150')
    elif(dir == 6): ser.write(b'M+255+255-100-100')
    elif(dir == 7): ser.write(b'M+255+255-000-000')

    if(dir == -1): ser.write(b'M+000+000+255+255')
    elif(dir == -2): ser.write(b'M-100-100+255+255')
    elif(dir == -3): ser.write(b'M-150-150+255+255')
    elif(dir == -4): ser.write(b'M-255-255+255+255') #back
    elif(dir == -5): ser.write(b'M-255-255+150+150')
    elif(dir == -6): ser.write(b'M-255-255+100+100')

    elif(dir == -7): ser.write(b'M-255-255+000+000')

def draw_wall(x , y):
    pygame.draw.rect(display, (100,100,255), (x , y, 10, 10))


#########################################################################################

last_x = x_robot
last_y = y_robot


var = 0
while not done:
    read_distance()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ser.write(b'M+255+255-255-255010 ')
    elif keys[pygame.K_s]:
        ser.write(b'M-255-255+255+255010 ')
    elif keys[pygame.K_d]:
        ser.write(b'M+255-255-255+255010 ')
    elif keys[pygame.K_a]:
        ser.write(b'M-255+255+255-255010 ')
    elif keys[pygame.K_SPACE]:
        ser.write(b'M+000+000-000-000000S')

    pygame.draw.circle(display, (255, 255, 255), (last_x, last_y), 20)
    pygame.draw.circle(display, (0, 255, 0), (x_robot, y_robot), 20)
    last_x = x_robot
    last_y = y_robot
    time.sleep(0.01)
    # print(distance.right, distance.left, distance.front)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ser.write(b'M+000+000-000-000000S')
            if event.key == pygame.K_UP:
                ser.write(b'M+255+255-255-255010S')
                while ser.read() != 'A':
                    pass
                time.sleep(0.01)
                y_robot -= 10
            if event.key == pygame.K_DOWN:
                ser.write(b'M-255-255+255+255010S')
                while ser.read() != 'A':
                    pass
                time.sleep(0.01)
                y_robot += 10
            if event.key == pygame.K_LEFT:
                ser.write(b'M-255+255+255-255010S')
                while ser.read() != 'A':
                    pass
                time.sleep(0.01)
                x_robot -= 10
            if event.key == pygame.K_RIGHT:
                ser.write(b'M+255-255-255+255010S')
                while ser.read() != 'A':
                    pass
                time.sleep(0.01)
                x_robot += 10
