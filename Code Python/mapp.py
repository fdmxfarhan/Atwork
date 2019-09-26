import serial
import time
import pygame

display = pygame.display.set_mode((800,600))
pygame.display.set_caption('IRA')

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout = 1)
#########################################################################################

class distance:
    right = -1
    left = -1
def read_distance():
    if(ser.read() == 'R'):
        distance.right = (ord(ser.read()) - 48) * 100
        distance.right += (ord(ser.read()) - 48) * 10
        distance.right += (ord(ser.read()) - 48) * 1

    if(ser.read() == 'L'):
        distance.left = (ord(ser.read()) - 48) * 100
        distance.left += (ord(ser.read()) - 48) * 10
        distance.left += (ord(ser.read()) - 48) * 1

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




#########################################################################################


direction = 's'
done = False
while not done:
    read_distance()

    

    # print(distance.right, distance.left)
    time.sleep(0.001)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                ser.write(b'M-255+255+255-255')
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                ser.write(b'M+255-255-255+255')
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                ser.write(b'M+255+255-255-255')
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                ser.write(b'M-255-255+255+255')
            elif event.key == pygame.K_1:
                move(1)
            elif event.key == pygame.K_2:
                move(2)
            elif event.key == pygame.K_3:
                move(3)
            elif event.key == pygame.K_4:
                move(4)
            elif event.key == pygame.K_5:
                move(5)
            elif event.key == pygame.K_6:
                move(6)
            elif event.key == pygame.K_7:
                move(7)
        if event.type == pygame.KEYUP:
            ser.write(b'M+000+000-000-000')
