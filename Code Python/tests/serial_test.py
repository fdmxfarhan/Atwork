import serial
import time
import pygame

display = pygame.display.set_mode((800,600))
pygame.display.set_caption('IRA')
class distance:
    right = -1

ser = serial.Serial('/dev/ttyUSB0', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout = 1)
direction = 's'
done = False
while not done:
    if(direction == 's'): ser.write(b'M+000+000+000+000')
    elif(direction == 'f'): ser.write(b'M+255+255-255-255')
    elif(direction == 'd'): ser.write(b'M-255-255+255+255')
    elif(direction == 'r'): ser.write(b'M+255-255-255+255')
    elif(direction == 'l'): ser.write(b'M-255+255+255-255')
    if(ser.read() == 'R'):
        distance.right = (ord(ser.read()) - 48) * 100
        distance.right += (ord(ser.read()) - 48) * 10
        distance.right += (ord(ser.read()) - 48) * 1


    print(distance.right)
    time.sleep(0.001)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                direction = 'l'
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                direction = 'r'
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                direction = 'f'
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                direction = 'd'

        if event.type == pygame.KEYUP:
            direction = 's'
