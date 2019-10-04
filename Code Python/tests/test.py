import pygame
import serial
import cv2
pygame.init()



display = pygame.display.set_mode((800,600))
pygame.display.set_caption('IRA')

def draw_wall(x , y):
    pygame.draw.circle(display, (100,100,255), (x , y), 8)
    pygame.draw.circle(display, (0,0,255), (x , y), 4)


drawing = False
done = False
while not done:
    mouse_position = pygame.mouse.get_pos()
    if drawing:
        draw_wall(mouse_position[0], mouse_position[1])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing = False

        # print(event)
