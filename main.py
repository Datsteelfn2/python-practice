import pygame
pygame.init()
# neccessary to use pygame
def display_score():
    time=int(pygame.time.get_ticks()/1000)-start_time
    converted_time=round(time,2)
    score_surface=test_font.render(f'{converted_time}',False,(64,64,64))
    score_rect=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    
start_time=0


width,height=800,400
screen=pygame.display.set_mode((width,height))
#how to display images below


test_font=pygame.font.Font(None,50)
'''text_surface=test_font.render("Python practice",False,(64,64,64))
text_rect=text_surface.get_rect(midtop=(400,50))'''

sky_surface=pygame.image.load('graphics/sky.png').convert_alpha() # we use convertalpha everytime we add an image, this is to make the images  easier to use for pygame, not big differnece for small games though
ground_surface=pygame.image.load('graphics/ground.png').convert_alpha()


clock=pygame.time.Clock()


snail_surface=pygame.image.load("graphics/snail/snail1.png").convert_alpha()
player_surface=pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
# we need to create rectangles to appropiatley place the player and snail on the ground, get rect method takes our surface and draws a rectangkle around it
player_rect=player_surface.get_rect(midbottom=(50,300))
snail_rect=snail_surface.get_rect(midbottom=(600,300))
player_stand=pygame.image.load("graphics/Player/player_stand.png").convert_alpha()



#intro screen
player_stand_rect=player_stand.get_rect(center=(400,200))


player_gravity=0


game_active=False




run=True
while run:
   
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        if game_active:
            if player_rect.bottom==300:

                if event.type==pygame.MOUSEBUTTONDOWN:
                    if player_rect.collidepoint(event.pos):
                        player_gravity=-20
                if event.type==pygame.KEYDOWN:# key down is when you press any key on the keyboard
                    if event.key==pygame.K_SPACE:
                        player_gravity=-20
        elif game_active==False:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RCTRL:
                    game_active=True
                    snail_rect.x=800
                    start_time=int(pygame.time.get_ticks()/1000)
     # runs as long as the player and snail dont collide   
    if game_active:
        
        screen.blit(sky_surface,(0,0))
        display_score()
        screen.blit(ground_surface,(0,300))
        '''pygame.draw.rect(screen,'#c0e8ec',text_rect)
        pygame.draw.rect(screen,'#c0e8ec',text_rect,10)'''
        
        screen.blit(snail_surface,snail_rect)
        screen.blit(player_surface,player_rect)
        #screen.blit(text_surface,text_rect)

        player_gravity+=1
        player_rect.y+=player_gravity
        #player_rect.left+=1
        snail_rect.x-=5
        if snail_rect.right<=0:
            snail_rect.left=800
        if player_rect.bottom>=300:
            player_rect.bottom=300
        #end game
        if player_rect.colliderect(snail_rect):
            game_active=False
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
    #collide rect is used to check if if the rectangles collide, this returns a 0 or 1, 0 means no collision and a 1 means there is a collision detected( can be used in if statement)


    #if (player_rect.colliderect(snail_rect))==True:
        #print('collision')
    
    
    #blit allows us to place one surface on another surface, here we put our surface on top of our screen(variable) surface
    #clock .tick 60 frames per second, frames are important
    clock.tick(60)
    pygame.display.update()
    # this updates everything including our screen variable