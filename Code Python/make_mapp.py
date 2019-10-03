import pygame

display = pygame.display.set_mode((800,600))
map = pygame.image.load('map.jpg')
display.blit(map, (0,0))
done = False
drawing = False
x1=0
y1=0
x2=0
y2=0

while not done:
    ms = pygame.mouse.get_pos()
    if drawing:
        pygame.draw.rect(display, (0,0,255), (x1,y1,x2-x1,y2-y1))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.image.save(display, "new_map.jpg")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x1 = ms[0]
                y1 = ms[1]
                drawing = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                x2 = ms[0]
                y2 = ms[1]
                drawing = True
