import pygame
pygame.init()
# neccessary to use pygame




width,height=800,400
screen=pygame.display.set_mode((width,height))
surface=pygame.image.load()



clock=pygame.time.Clock()
run=True
while run:
   
    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            run=False
    screen.blit(surface,(200,100))
    #blit allows us to place one surface on another surface, here we put our surface on top of our screen(variable) surface
    clock.tick(60)
    pygame.display.update()
    # this updates everything including our screen variable