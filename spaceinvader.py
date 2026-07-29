import math
import random
import pygame
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
enemy_start_y_max = 150
enemy_speed_x = 4
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background,(screen_width,screen_height))
pygame.display.set_caption('spaceinvader')
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)
player_img = pygame.image.load('player.png')
player_img = pygame.transform.scale(player_img,(64,64))
player_x = player_start_x
player_y = player_start_y
player_x_change = 0
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6
enemy_size = 50
for i in range(num_of_enemies):
    enemy_img.append(pygame.transform.scale(pygame.image.load('enemy.png'),(enemy_size,enemy_size)))
    enemy_x.append(random.randint(0,screen_width-enemy_size))
    enemy_y.append(random.randint(enemy_start_y_min,enemy_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)
bullet_img = pygame.image.load('bullet.png')
bullet_img = pygame.transform.scale(bullet_img,(16,32))
bullet_x = 0
bullet_y = player_start_y
bullet_state = 'ready'
score = 0
font = pygame.font.Font("freesansbold.ttf",32)
game_over = pygame.font.Font("freesansbold.ttf",64)
running = True
while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            elif event.key == pygame.K_RIGHT:
                player_x_change = +5
            elif event.key == pygame.K_SPACE and bullet_state == 'ready':
                bullet_x = player_x
                bullet_state = 'fire'
        elif event.type == pygame.KEYUP:
            player_x_change = 0
    player_x += player_x_change
    player_x = max(0,min(player_x,screen_width-64))
    if bullet_state == 'fire':
        screen.blit(bullet_img,(bullet_x+16,bullet_y+10))
        bullet_y-= bullet_speed_y
    if bullet_y <=0:
        bullet_y = player_start_y
        bullet_state = 'ready'
    for i in range(num_of_enemies):
        enemy_x[i]+= enemy_x_change[i] 
        if enemy_x[i] <= 0 or enemy_x[i] >= screen_width-enemy_size:
            enemy_x_change[i] *= -1
            enemy_y[i] += enemy_speed_y
        if math.hypot(enemy_x[i] - bullet_x, enemy_y[i] - bullet_y) < collision_distance:
            score+= 1
            bullet_y = player_start_y
            bullet_state = 'ready'
            enemy_x[i] = random.randint(0,screen_width-enemy_size)
            enemy_y[i] = random.randint(enemy_start_y_min,enemy_start_y_max)
        if enemy_y[i] > 340:
            screen.blit(game_over.render("GAME OVER",True,(255,255,255)),(180,220))
            running = False
        screen.blit(enemy_img[i],(enemy_x[i],enemy_y[i]))
    screen.blit(player_img,(player_x,player_y))
    screen.blit(font.render(f"score:{score}",True,(255,255,255)),(10,10))
    pygame.display.update()
    clock.tick(60)
pygame.quit()