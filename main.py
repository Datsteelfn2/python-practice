import pygame
import random
pygame.init()
# neccessary to use pygame

    
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



#intro screen
player_stand=pygame.image.load("graphics/Player/player_stand.png").convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect=player_stand.get_rect(center=(400,200))

title_text=test_font.render("Snail-Dash",0,"Black")
title_text_rect=title_text.get_rect(center=(400,80))

game_instructions=test_font.render("Press space to run",0,"Black")                                  
game_instructions_rect=game_instructions.get_rect(center=(400,330))

score=0
fly_surface=pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()

def display_score():
    time=int(pygame.time.get_ticks()/1000)-start_time
    converted_time=round(time,2)
    score_surface=test_font.render(f'{converted_time}',False,(64,64,64))
    score_rect=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    return time
def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=4
            if obstacle_rect.bottom==300:

                screen.blit(snail_surface,obstacle_rect)
            else:
                screen.blit(fly_surface,obstacle_rect)
        obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-100]
        return obstacle_list
    else:
        return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True
#obstacles


#timer
obstacle_timer=pygame.USEREVENT +1# need to include + 1
pygame.time.set_timer(obstacle_timer,1500)

obstacle_rect_list=[]


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
                    
                    start_time=int(pygame.time.get_ticks()/1000)
        if event.type==obstacle_timer and game_active:
            if random.randint(0,2):
                obstacle_rect_list.append(snail_surface.get_rect(midbottom=(random.randint(900,1100),300)))
            else:
                obstacle_rect_list.append(fly_surface.get_rect(midbottom=(random.randint(900,1100),210)))
     # runs as long as the player and snail dont collide   
    if game_active:
        
        screen.blit(sky_surface,(0,0))
        score=display_score()
        screen.blit(ground_surface,(0,300))
        '''pygame.draw.rect(screen,'#c0e8ec',text_rect)
        pygame.draw.rect(screen,'#c0e8ec',text_rect,10)'''
        
        
        screen.blit(player_surface,player_rect)
        #screen.blit(text_surface,text_rect)

        player_gravity+=1
        player_rect.y+=player_gravity
        #player_rect.left+=1
        
        if player_rect.bottom>=300:
            player_rect.bottom=300
        #end game
        #obstacle
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)
        game_active=collisions(player_rect,obstacle_rect_list)
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        screen.blit(title_text,title_text_rect)
        
        score_message=test_font.render(f"Your score {score}",0,"Black")
        score_message_rect=score_message.get_rect(center=(400,330))
        if score==0:
            screen.blit(game_instructions,game_instructions_rect)
            
        else:
            screen.blit(score_message,score_message_rect)
            
    #collide rect is used to check if if the rectangles collide, this returns a 0 or 1, 0 means no collision and a 1 means there is a collision detected( can be used in if statement)


    #if (player_rect.colliderect(snail_rect))==True:
        #print('collision')
    
    
    
    #blit allows us to place one surface on another surface, here we put our surface on top of our screen(variable) surface
    #clock .tick 60 frames per second, frames are important
    clock.tick(60)
    pygame.display.update()
    # this updates everything including our screen variable