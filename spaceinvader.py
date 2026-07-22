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
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('background.jpg')
pygame.display.set_caption('spaceinvader')
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)
player_img = pygame.image.load('player.png')
player_x = player_start_x
player_y = player_start_y
player_x_change = 0
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemies = 6
