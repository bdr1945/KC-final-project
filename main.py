import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((400, 720))
pygame.display.set_caption('king of the mountain')
clock = pygame.time.Clock()
cave = pygame.image.load('sprite/background.png').convert_alpha()
test_font = pygame.font.Font('sprite/Pixeltype.ttf', 50)
roock = pygame.image.load('sprite/longer rock platform.png').convert_alpha()
rock = pygame.image.load('sprite/rock platform.png').convert_alpha()
ground = pygame.image.load('sprite/ground.png').convert_alpha()
boy = pygame.image.load('sprite/boy.png').convert_alpha()
flag = pygame.image.load('sprite/Finish_flag.png').convert_alpha() # changed from 'finish_flag.png' to 'Finish_flag.png'
boy_y = 560
boy_vel_x = 0
boy_vel_y = 0
jumping = True
jump_power = 20
left = True
right = True
rock_rects = [rock.get_rect(midbottom=(298, 534)), roock.get_rect(midbottom=(203, 587)), rock.get_rect(midbottom=(217, 439)), roock.get_rect(midbottom=(303, 293)), rock.get_rect(midbottom=(183, 243)), rock.get_rect(midbottom=(67, 207)), rock.get_rect(midbottom=(140, 129))]
ground_rect = ground.get_rect(midbottom=(200,700))
boy_rect = boy.get_rect(midbottom=(200,700))
flag_rect = flag.get_rect(topleft=(0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                boy_vel_x += 5
            if event.key == pygame.K_a:
                boy_vel_x -= 5
            if event.key == pygame.K_SPACE and not jumping:
                boy_vel_y -= jump_power
                jumping = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                boy_vel_x -= 5
            if event.key == pygame.K_a:
                boy_vel_x += 5

    boy_rect.x += boy_vel_x
    boy_rect.y += boy_vel_y

    if boy_rect.collidelist(rock_rects) != -1 or boy_rect.colliderect(ground_rect):
        jumping = False
        boy_vel_y = 0
    else:
        jumping = True
        boy_vel_y += 1

    screen.blit(cave, (0, 0))
    for rect in rock_rects:
        screen.blit(rock, rect)
    screen.blit(ground, ground_rect)
    screen.blit(flag, flag_rect)
    screen.blit(boy, boy_rect)

    if boy_rect.colliderect(flag_rect):
        win_screen = pygame.Surface((400,720))
        win_screen.fill((0,0,0))
        win_text_surface = test_font.render('You Win!!', False, (255,255,255))
        win_text_rect = win_text_surface.get_rect(center=(200,360))
        win_screen.blit(win_text_surface, win_text_rect)
        screen.blit(win_screen,(0,0))

    pygame.display.update()
    clock.tick(60)




    







