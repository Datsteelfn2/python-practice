import pygame
pygame.init()
# neccessary to use pygame




width,height=800,400
screen=pygame.display.set_mode((width,height))
#how to display images below

test_font=pygame.font.Font("font/Pixeltype.ttf",50)

sky_surface=pygame.image.load('graphics/sky.png').convert_alpha() # we use convertalpha everytime we add an image, this is to make the images  easier to use for pygame, not big differnece for small games though
ground_surface=pygame.image.load('graphics/ground.png').convert_alpha()
text_surface=test_font.render("Python practice",False,'Black')
snail_surface=pygame.image.load("graphics/snail/snail1.png").convert_alpha()
clock=pygame.time.Clock()


snail_x_pos=600
velocity=5

player_surface=pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
# we need to create rectangles to appropiatley place the player and snail on the ground, get rect method takes our surface and draws a rectangkle around it
player_rect=player_surface.get_rect(midbottom=(50,300))
snai_rect=snail_surface.get_rect(midbottom=(snail_x_pos,300))


run=True
while run:
   
    for even in pygame.event.get():
        if even.type==pygame.QUIT:
            run=False
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    if snail_x_pos<-100:
        snail_x_pos=800
    snail_x_pos-=velocity
    screen.blit(snail_surface,snai_rect)
    screen.blit(player_surface,player_rect)

    #blit allows us to place one surface on another surface, here we put our surface on top of our screen(variable) surface
    #clock .tick 60 frames per second, frames are important
    clock.tick(60)
    pygame.display.update()
    # this updates everything including our screen variable